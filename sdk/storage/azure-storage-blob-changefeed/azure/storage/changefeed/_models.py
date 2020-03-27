# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-few-public-methods, too-many-instance-attributes
# pylint: disable=super-init-not-called, too-many-lines
import json
import collections
from io import BytesIO

from avro.datafile import DataFileReader
from avro.io import DatumReader

from azure.core.exceptions import HttpResponseError
from azure.core.paging import PageIterator, ItemPaged

from ._shared import decode_base64_to_text
from ._shared.response_handlers import return_context_and_deserialized, process_storage_error


class ChangeFeedPaged(PageIterator):
    """An Iterable of Blob properties.

    :ivar str service_endpoint: The service URL.
    :ivar str prefix: A blob name prefix being used to filter the list.
    :ivar str marker: The continuation token of the current page of results.
    :ivar int results_per_page: The maximum number of results retrieved per API call.
    :ivar str continuation_token: The continuation token to retrieve the next page of results.
    :ivar str location_mode: The location mode being used to list results. The available
        options include "primary" and "secondary".
    :ivar current_page: The current page of listed results.
    :vartype current_page: list(~azure.storage.blob.BlobProperties)
    :ivar str container: The container that the blobs are listed from.
    :ivar str delimiter: A delimiting character used for hierarchy listing.

    :param callable command: Function to retrieve the next page of items.
    :param str container: The name of the container.
    :param str prefix: Filters the results to return only blobs whose names
        begin with the specified prefix.
    :param int results_per_page: The maximum number of blobs to retrieve per
        call.
    :param str continuation_token: An opaque continuation token.
    :param str delimiter:
        Used to capture blobs whose names begin with the same substring up to
        the appearance of the delimiter character. The delimiter may be a single
        character or a string.
    :param location_mode: Specifies the location the request should be sent to.
        This mode only applies for RA-GRS accounts which allow secondary read access.
        Options include 'primary' or 'secondary'.
    """
    def __init__(
            self, container_client,
            results_per_page=None,
            start_time=None,
            end_time=None,
            continuation_token=None,
            delimiter=None,
            location_mode=None):
        super(ChangeFeedPaged, self).__init__(
            get_next=self._get_next,
            extract_data=self._extract_data_cb,
            continuation_token=continuation_token or ""
        )
        # self.container_client = container_client
        # self.service_endpoint = None
        self.marker = None
        self.results_per_page = results_per_page or 500
        self.current_page = None
        self._change_feed = ChangeFeed(container_client, self.results_per_page)
        # self.location_mode = location_mode

    def _get_next(self, continuation_token):
        try:
            return next(self._change_feed)
        except HttpResponseError as error:
            # we need to wrap the error
            process_storage_error(error)

    def _extract_data_cb(self, event_list):
        self.current_page = [self._build_item(item) for item in event_list]
        # TODO: make it accurate
        if self.current_page:
            return '', self.current_page
        return None, self.current_page

    def _build_item(self, item):
    #     if isinstance(item, BlobProperties):
    #         return item
    #     if isinstance(item, BlobItem):
    #         blob = BlobProperties._from_generated(item)  # pylint: disable=protected-access
    #         blob.container = self.container
    #         return blob
        return item


class ChangeFeed(object):
    def __init__(self, client, page_size):
        self.client = client
        self.page_size = page_size
        self.unprocessed_segment_paths = []
        self.current_segment = None
        self._initialize()

    def __iter__(self):
        return self

    def __next__(self):
        change_feed = []
        remaining_to_load = self.page_size

        # reset the current segment page size. The page size which was set to remaining_to_load in the last call
        # could be very small
        if not self.current_segment:
            return change_feed
        else:
            self.current_segment.page_size = self.page_size

        while len(change_feed) < self.page_size and self.current_segment:
            page_of_events = next(self.current_segment)
            # can we append a list to another list?????
            change_feed.extend(page_of_events)
            remaining_to_load -= len(page_of_events)
            if not remaining_to_load:
                return change_feed
            self.current_segment = self._get_next_segment(remaining_to_load)

        return change_feed

    next = __next__  # Python 2 compatibility.

    def _initialize(self):
        self.unprocessed_segment_paths = list(self.client.list_blobs(
            name_starts_with="idx/segments/"))
        self.current_segment = self._get_next_segment(self.page_size)

    def _get_next_segment(self, page_size):
        if self.unprocessed_segment_paths:
            segment_path = self.unprocessed_segment_paths.pop(0)
            return Segment(self.client, segment_path, page_size)
        return None


class Segment(object):
    def __init__(self, client, segment_path, page_size):
        self.client = client
        self.segment_path = segment_path
        self.page_size = page_size
        self.shards = collections.deque()
        self._initialize()

    def __iter__(self):
        return self

    def __next__(self):
        segment_events = []
        while len(segment_events) < self.page_size and self.shards:
            shard = self.shards.popleft()
            event = next(shard)
            if event:
                segment_events.append(event)
                self.shards.append(shard)
        return segment_events

    next = __next__  # Python 2 compatibility.

    def _initialize(self):
        segment_content = self.client.get_blob_client(self.segment_path).download_blob().readall()
        segment_content = segment_content.decode()
        segment_dict = json.loads(segment_content)
        shard_paths = segment_dict['chunkFilePaths']
        # we can initiate shards in parallel
        for shard_path in shard_paths:
            self.shards.append(Shard(self.client, shard_path))


class Shard(object):
    def __init__(self, client, shard_path):
        self.client = client
        self.shard_path = shard_path
        self.current_chunk = None
        self.unprocessed_chunk_paths = []
        self._initialize()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current_chunk:
            return None
        next_event = next(self.current_chunk)
        while not next_event and self.unprocessed_chunk_paths:
            self.current_chunk = self._get_next_chunk()
            next_event = next(self.current_chunk)
        return next_event

    next = __next__  # Python 2 compatibility.

    def _initialize(self):
        # To get all chunk file paths
        shard_path = self.shard_path.replace('$blobchangefeed/', '', 1)
        self.unprocessed_chunk_paths = list(self.client.list_blobs(name_starts_with=shard_path))
        self.current_chunk = self._get_next_chunk()

    def _get_next_chunk(self):
        if self.unprocessed_chunk_paths:
            current_chunk_path = self.unprocessed_chunk_paths.pop(0)
            return Chunk(self.client, current_chunk_path)
        return None


class Chunk(object):
    def __init__(self, client, chunk_path):
        self.client = client
        self.chunk_path = chunk_path
        self.file_reader = None
        self._initialize()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.file_reader)
        except StopIteration:
            return None

    next = __next__  # Python 2 compatibility.

    def _initialize(self):
        # To get all events in a chunk
        file_content = self.client.get_blob_client(self.chunk_path).download_blob().readall()
        self.file_reader = DataFileReader(BytesIO(file_content), DatumReader())
