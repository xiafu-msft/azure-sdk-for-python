# Stubs for azure.storage.fileshare._shared.policies_async (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .policies import StorageRetryPolicy, is_retry
from azure.core.pipeline import PipelineRequest, PipelineResponse
from azure.core.pipeline.policies import AsyncHTTPPolicy
from typing import Any

async def retry_hook(settings: Any, **kwargs: Any) -> None: ...

class AsyncStorageResponseHook(AsyncHTTPPolicy):
    def __init__(self, **kwargs: Any) -> None: ...
    async def send(self, request: PipelineRequest) -> PipelineResponse: ...

class AsyncStorageRetryPolicy(StorageRetryPolicy):
    async def sleep(self, settings: Any, transport: Any) -> None: ...
    async def send(self, request: Any): ...

class ExponentialRetry(AsyncStorageRetryPolicy):
    initial_backoff: Any = ...
    increment_base: Any = ...
    random_jitter_range: Any = ...
    def __init__(self, initial_backoff: int = ..., increment_base: int = ..., retry_total: int = ..., retry_to_secondary: bool = ..., random_jitter_range: int = ..., **kwargs: Any) -> None: ...
    def get_backoff_time(self, settings: Any): ...

class LinearRetry(AsyncStorageRetryPolicy):
    backoff: Any = ...
    random_jitter_range: Any = ...
    def __init__(self, backoff: int = ..., retry_total: int = ..., retry_to_secondary: bool = ..., random_jitter_range: int = ..., **kwargs: Any) -> None: ...
    def get_backoff_time(self, settings: Any): ...
