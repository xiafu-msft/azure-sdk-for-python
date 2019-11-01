# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import DataLakeStorageClientConfiguration
from azure.core.exceptions import map_error
from .operations_async import ServiceOperations
from .operations_async import FileSystemOperations
from .operations_async import PathOperations
from .. import models


class DataLakeStorageClient(object):
    """Azure Data Lake Storage provides storage for Hadoop and other big data workloads.


    :ivar service: Service operations
    :vartype service: azure.storage.file.datalake.aio.operations_async.ServiceOperations
    :ivar file_system: FileSystem operations
    :vartype file_system: azure.storage.file.datalake.aio.operations_async.FileSystemOperations
    :ivar path: Path operations
    :vartype path: azure.storage.file.datalake.aio.operations_async.PathOperations

    :param url: The URL of the service account, container, or blob that is the
     targe of the desired operation.
    :type url: str
    :param file_system: The filesystem identifier.
    :type file_system: str
    :param path1: The file or directory path.
    :type path1: str
    """

    def __init__(
            self, url, file_system, path1, **kwargs):

        base_url = '{url}'
        self._config = DataLakeStorageClientConfiguration(url, file_system, path1, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-11-09'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_system = FileSystemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.path = PathOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
