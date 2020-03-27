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


class ContainerSamples(object):

    connection_string = "o	DefaultEndpointsProtocol=https;AccountName=seanchangefeedstage;AccountKey=XbDHF5F/HxkQ8gil8QvI99D07ppEN64lBQOuU0h68T//hps7C2Iu+UUviIQgK6vSKGD22dmn4ohXaVg7DhUFIA==;EndpointSuffix=core.windows.net"

    #--Begin Blob Samples-----------------------------------------------------------------

    def list_blobs_in_container(self):

        # Instantiate a BlobServiceClient using a connection string
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

        # Instantiate a ContainerClient
        container_client = blob_service_client.get_container_client("myblobscontainer8")

        # Create new Container
        container_client.create_container()

        # [START upload_blob_to_container]
        with open(SOURCE_FILE, "rb") as data:
            blob_client = container_client.upload_blob(name="myblob", data=data)

        # container_client.get_blob_client("blobchangefeed1").create_append_blob()
        # container_client.get_blob_client("blobchangefeed2").create_append_blob()
        # properties = blob_client.get_blob_properties()
        # [END upload_blob_to_container]

        # [START list_blobs_in_container]
        container_client2 = blob_service_client.get_container_client("$blobchangefeed")
        blobs_list = container_client2.list_blobs(name_starts_with='idx/segments/2020/03/25')
        # blobs_list = container_client2.list_blobs()

        try:
            for blob in blobs_list:
                # print(blob.name + '\n')
                # get segment content
                content = container_client2.get_blob_client(blob.name).download_blob().readall()
                segment_content = content.decode()
                segment_dict = json.loads(segment_content)

                # get chunk file paths
                chunk_file_paths = segment_dict['chunkFilePaths']

                for chunk_file_path in chunk_file_paths:
                    chunk_file_path = chunk_file_path.replace('$blobchangefeed/', '', 1)
                    # get chunks
                    change_feed_file_paths = container_client2.list_blobs(name_starts_with=chunk_file_path)
                    for change_feed_file_path in change_feed_file_paths:
                        file_content = container_client2.get_blob_client(change_feed_file_path.name).download_blob()
                        data = file_content.readall()
                        print(file_content)
                        stream = DataFileReader(BytesIO(data), DatumReader())
                        data = next(stream)
                        while data:
                            print(data)
                            data = next(stream)
        except Exception as e:
            print("error")
        # [END list_blobs_in_container]




        content = container_client2.get_blob_client("idx/segments/2020/03/24/2300/meta.json").download_blob().readall()

        segment_content = content.decode()

        segment_dict = json.loads(segment_content)
        # print(segment_dict)

        # Delete container
        container_client.delete_container()


if __name__ == '__main__':
    sample = ContainerSamples()
    chunks = deque()
    if not chunks:
        print("empty")
    chunks.append("a")
    if chunks:
        print("a")
