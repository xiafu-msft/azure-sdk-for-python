# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from collections import deque
from io import BytesIO

from avro.datafile import DataFileReader
from avro.io import DatumReader
from azure.storage.changefeed import ChangeFeedClient

"""
FILE: blob_samples_container.py
DESCRIPTION:
    This sample demonstrates common container operations including list blobs, create a container,
    set metadata etc.
USAGE:
    python blob_samples_container.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""

import os
from datetime import datetime, timedelta

from azure.core.exceptions import ResourceExistsError

SOURCE_FILE = 'SampleSource.txt'


class ChangeFeedSamples(object):
    connection_string = "o	DefaultEndpointsProtocol=https;AccountName=seanchangefeedstage;AccountKey=XbDHF5F/HxkQ8gil8QvI99D07ppEN64lBQOuU0h68T//hps7C2Iu+UUviIQgK6vSKGD22dmn4ohXaVg7DhUFIA==;EndpointSuffix=core.windows.net"

    def list_events_by_page(self):

        # Instantiate a BlobServiceClient using a connection string

        cf_client = ChangeFeedClient("http://seanchangefeedstage.blob.core.windows.net",
                                     credential="XbDHF5F/HxkQ8gil8QvI99D07ppEN64lBQOuU0h68T//hps7C2Iu+UUviIQgK6vSKGD22dmn4ohXaVg7DhUFIA==")
        change_feed = cf_client.get_changes().by_page()

        # print first page of events
        change_feed_page1 = next(change_feed)
        events_per_page = list(change_feed_page1)
        for event in events_per_page:
            print(event)

        # print second page of events
        change_feed_page2 = next(change_feed)
        events_per_page = list(change_feed_page2)
        for event in events_per_page:
            print(event)

    def list_all_events(self):
        cf_client = ChangeFeedClient("http://seanchangefeedstage.blob.core.windows.net",
                                     credential="XbDHF5F/HxkQ8gil8QvI99D07ppEN64lBQOuU0h68T//hps7C2Iu+UUviIQgK6vSKGD22dmn4ohXaVg7DhUFIA==")
        change_feed = cf_client.get_changes().by_page()

        # print first page of events
        change_feed_pages = list(change_feed)
        for event_page in change_feed_pages:
            for event in event_page:
                print(event)


if __name__ == '__main__':
    sample = ChangeFeedSamples()
    # sample.list_events()
    sample.list_all_events()
    # TODO: REMOVE STUFF BELOW, THIS IS ONLY FOR TEST
    aaaa = [1, 2, 3, 4]
    print(aaaa)
