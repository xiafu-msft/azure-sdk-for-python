# Stubs for datalake._data_lake_file_client (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from azure.storage.file.datalake._path_client import PathClient
from typing import Any, Optional

class DataLakeFileClient(PathClient):
    def __init__(self, account_url: str, file_system_name: str, file_directory: str, file_name: str, credential: Optional[Any]=..., **kwargs: Any) -> Any: ...
    @classmethod
    def from_connection_string(cls: Any, conn_str: str, file_system_name: str, directory_name: str, file_name: str, credential: Optional[Any]=..., **kwargs: Any) -> DataLakeFileClient: ...
    def create_file(self, content_settings: Optional[ContentSettings]=..., metadata: Optional[Dict[str, str]]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def delete_file(self, **kwargs: Any) -> None: ...
    def get_file_properties(self, **kwargs: Any) -> FileProperties: ...
    def append_data(self, data: Union[AnyStr, Iterable[AnyStr], IO[AnyStr]], offset: int, length: Optional[int]=..., **kwargs: Any) -> Dict[str, Union[str, datetime, int]]: ...
    def flush_data(self, offset: int, retain_uncommitted_data: Optional[bool]=..., **kwargs: Any) -> Dict[str, Union[str, datetime]]: ...
    def read_file(self, offset: Optional[int]=..., length: Optional[int]=..., stream: Optional[IO]=..., **kwargs: Any) -> Union[int, byte, str]: ...
