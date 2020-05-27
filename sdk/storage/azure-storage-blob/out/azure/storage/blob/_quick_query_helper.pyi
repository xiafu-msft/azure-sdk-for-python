# Stubs for azure.storage.blob._quick_query_helper (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._models import QuickQueryError
from ._shared.avro.avro_io import DatumReader
from ._shared.avro.datafile import DataFileReader
from typing import Any, Optional

class QuickQueryReader:
    name: Any = ...
    container: Any = ...
    response_headers: Any = ...
    total_bytes: Any = ...
    bytes_processed: int = ...
    def __init__(self, client: Optional[Any] = ..., name: Optional[Any] = ..., container: Optional[Any] = ..., progress_callback: Optional[Any] = ..., encoding: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def __len__(self): ...
    def readall(self): ...
    def readinto(self, stream: Any) -> None: ...

class QuickQueryStreamer:
    generator: Any = ...
    iterator: Any = ...
    leftover: bytes = ...
    file_length: Any = ...
    def __init__(self, generator: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def seekable(self): ...
    def next(self): ...
    def tell(self): ...
    def seek(self, offset: Any, whence: int = ...) -> None: ...
    def read(self, size: Any): ...
