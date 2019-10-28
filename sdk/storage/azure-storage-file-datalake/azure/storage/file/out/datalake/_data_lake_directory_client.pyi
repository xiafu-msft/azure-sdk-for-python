# Stubs for datalake._data_lake_directory_client (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._path_client import PathClient
from azure.storage.file.datalake import DataLakeFileClient
from typing import Any, Optional

class DataLakeDirectoryClient(PathClient):
    def __init__(self, account_url: str, file_system_name: str, directory_name: str, credential: Optional[Any]=..., **kwargs: Any) -> Any: ...
    def generate_shared_access_signature(self) -> None: ...
    @classmethod
    def from_connection_string(cls: Any, conn_str: str, file_system_name: str, directory_name: str, credential: Optional[Any]=..., **kwargs: Any) -> DataLakeDirectoryClient: ...
    def create_directory(self, content_settings: Optional[ContentSettings]=..., metadata: Optional[Dict[str, str]]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def delete_directory(self, **kwargs: Any) -> ItemPaged[Response]: ...
    def get_directory_properties(self, **kwargs: Any) -> DirectoryProperties: ...
    def create_sub_directory(self, sub_directory: Union[DirectoryProperties, str], content_settings: Optional[ContentSettings]=..., metadata: Optional[Dict[str, str]]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def delete_sub_directory(self, sub_directory: Union[DirectoryProperties, str], **kwargs: Any) -> ItemPaged[Response]: ...
    def get_file_client(self, file: Union[FileProperties, str]) -> DataLakeFileClient: ...
    def get_sub_directory_client(self, sub_directory: Union[DirectoryProperties, str]) -> DataLakeDirectoryClient: ...
