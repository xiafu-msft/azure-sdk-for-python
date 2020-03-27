# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines,no-self-use
import functools
from typing import (  # pylint: disable=unused-import
    Optional, Any, TYPE_CHECKING
)

from azure.core.paging import ItemPaged

from azure.storage.blob import BlobServiceClient

try:
    from urllib.parse import urlparse, quote, unquote
except ImportError:
    from urlparse import urlparse # type: ignore
    from urllib2 import quote, unquote # type: ignore

from ._models import ChangeFeedPaged
if TYPE_CHECKING:
    pass

_ERROR_UNSUPPORTED_METHOD_FOR_ENCRYPTION = (
    'The require_encryption flag is set, but encryption is not supported'
    ' for this method.')


class ChangeFeedClient(object):  # pylint: disable=too-many-public-methods
    """A client to interact with a specific blob, although that blob may not yet exist.

    :param str account_url:
        The URI to the storage account. In order to create a client given the full URI to the blob,
        use the :func:`from_blob_url` classmethod.
    :param container_name: The container name for the blob.
    :type container_name: str
    :param blob_name: The name of the blob with which to interact. If specified, this value will override
        a blob value specified in the blob URL.
    :type blob_name: str
    :param str snapshot:
        The optional blob snapshot on which to operate. This can be the snapshot ID string
        or the response returned from :func:`create_snapshot`.
    :param credential:
        The credentials with which to authenticate. This is optional if the
        account URL already has a SAS token. The value can be a SAS token string, an account
        shared access key, or an instance of a TokenCredentials class from azure.identity.
        If the URL already has a SAS token, specifying an explicit credential will take priority.
    :keyword str api_version:
        The Storage API version to use for requests. Default value is '2019-07-07'.
        Setting to an older version may result in reduced feature compatibility.

        .. versionadded:: 12.2.0

    :keyword str secondary_hostname:
        The hostname of the secondary endpoint.
    :keyword int max_block_size: The maximum chunk size for uploading a block blob in chunks.
        Defaults to 4*1024*1024, or 4MB.
    :keyword int max_single_put_size: If the blob size is less than max_single_put_size, then the blob will be
        uploaded with only one http PUT request. If the blob size is larger than max_single_put_size,
        the blob will be uploaded in chunks. Defaults to 64*1024*1024, or 64MB.
    :keyword int min_large_block_upload_threshold: The minimum chunk size required to use the memory efficient
        algorithm when uploading a block blob. Defaults to 4*1024*1024+1.
    :keyword bool use_byte_buffer: Use a byte buffer for block blob uploads. Defaults to False.
    :keyword int max_page_size: The maximum chunk size for uploading a page blob. Defaults to 4*1024*1024, or 4MB.
    :keyword int max_single_get_size: The maximum size for a blob to be downloaded in a single call,
        the exceeded part will be downloaded in chunks (could be parallel). Defaults to 32*1024*1024, or 32MB.
    :keyword int max_chunk_get_size: The maximum chunk size used for downloading a blob. Defaults to 4*1024*1024,
        or 4MB.

    .. admonition:: Example:

        .. literalinclude:: ../samples/blob_samples_authentication.py
            :start-after: [START create_blob_client]
            :end-before: [END create_blob_client]
            :language: python
            :dedent: 8
            :caption: Creating the BlobClient from a URL to a public blob (no auth needed).

        .. literalinclude:: ../samples/blob_samples_authentication.py
            :start-after: [START create_blob_client_sas_url]
            :end-before: [END create_blob_client_sas_url]
            :language: python
            :dedent: 8
            :caption: Creating the BlobClient from a SAS URL to a blob.
    """
    def __init__(
            self, account_url,  # type: str
            credential=None,  # type: Optional[Any]
            **kwargs  # type: Any
        ):
        # type: (...) -> None
        self._blob_service_client = BlobServiceClient(account_url, credential, **kwargs)

    def get_changes(self, start_time=None, end_time=None, continuation=None, **kwargs):

        timeout = kwargs.pop('timeout', None)
        container_client = self._blob_service_client.get_container_client("$blobchangefeed")
        return ItemPaged(
            container_client,
            results_per_page=None,
            start_time=start_time,
            end_time=end_time,
            page_iterator_class=ChangeFeedPaged)


