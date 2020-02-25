# Stubs for azure.storage.filedatalake._file_system_client (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._data_lake_directory_client import DataLakeDirectoryClient
from ._data_lake_file_client import DataLakeFileClient
from ._data_lake_lease import DataLakeLeaseClient
from ._generated import DataLakeStorageClient
from ._models import FileSystemProperties, LocationMode, PathPropertiesPaged
from ._serialize import convert_dfs_url_to_blob_url
from ._shared.base_client import StorageAccountHostsMixin, parse_connection_str, parse_query
from azure.core.paging import ItemPaged
from typing import Any, Optional

class FileSystemClient(StorageAccountHostsMixin):
    file_system_name: Any = ...
    def __init__(self, account_url: str, file_system_name: str, credential: Optional[Any]=..., **kwargs: Any) -> None: ...
    @classmethod
    def from_connection_string(cls: Any, conn_str: str, file_system_name: str, credential: Optional[Any]=..., **kwargs: Any) -> FileSystemClient: ...
    def acquire_lease(self, lease_duration: int=..., lease_id: Optional[str]=..., **kwargs: Any) -> DataLakeLeaseClient: ...
    def create_file_system(self, metadata: Optional[Dict[str, str]]=..., public_access: Optional[PublicAccess]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def delete_file_system(self, **kwargs: Any) -> None: ...
    def get_file_system_properties(self, **kwargs: Any) -> FileSystemProperties: ...
    def set_file_system_metadata(self, metadata: Optional[Dict[str, str]]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def get_paths(self, path: Optional[str]=..., recursive: Optional[bool]=..., max_results: Optional[int]=..., **kwargs: Any) -> ItemPaged[PathProperties]: ...
    def create_directory(self, directory: Union[DirectoryProperties, str], content_settings: Optional[ContentSettings]=..., metadata: Optional[Dict[str, str]]=..., **kwargs: Any) -> DataLakeDirectoryClient: ...
    def delete_directory(self, directory: Union[DirectoryProperties, str], **kwargs: Any) -> DataLakeDirectoryClient: ...
    def create_file(self, file: Union[FileProperties, str], **kwargs: Any) -> DataLakeFileClient: ...
    def delete_file(self, file: Union[FileProperties, str], lease: Optional[Union[DataLakeLeaseClient, str]]=..., **kwargs: Any) -> DataLakeFileClient: ...
    def set_file_system_access_policy(self, signed_identifiers: Dict[str, AccessPolicy], public_access: Optional[Union[str, PublicAccess]]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def get_root_directory_client(self) -> DataLakeDirectoryClient: ...
    def get_directory_client(self, directory: Union[DirectoryProperties, str]) -> DataLakeDirectoryClient: ...
    def get_file_client(self, file_path: Union[FileProperties, str]) -> DataLakeFileClient: ...
