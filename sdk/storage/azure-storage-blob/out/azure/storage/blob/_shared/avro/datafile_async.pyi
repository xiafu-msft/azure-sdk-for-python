# Stubs for azure.storage.blob._shared.avro.datafile_async (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..avro import avro_io_async, schema
from .datafile import DataFileException, MAGIC, META_SCHEMA, SCHEMA_KEY, SYNC_SIZE
from typing import Any

PY3: Any
logger: Any
VALID_CODECS: Any

class AsyncDataFileReader:
    codec: str = ...
    def __init__(self, reader: Any, datum_reader: Any, **kwargs: Any) -> None: ...
    async def init(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, data_type: Any, value: Any, traceback: Any) -> None: ...
    def __aiter__(self): ...
    @property
    def reader(self): ...
    @property
    def raw_decoder(self): ...
    @property
    def datum_decoder(self): ...
    @property
    def datum_reader(self): ...
    @property
    def sync_marker(self): ...
    @property
    def meta(self): ...
    @property
    def block_count(self): ...
    def get_meta(self, key: Any): ...
    async def __anext__(self): ...
    def close(self) -> None: ...
