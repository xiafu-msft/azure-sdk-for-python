# Stubs for azure.storage.blob._serialize (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._generated.models import ContainerCpkScopeInfo, CpkScopeInfo, ModifiedAccessConditions, SourceModifiedAccessConditions
from ._models import ContainerEncryptionScope
from typing import Any

def get_modify_conditions(kwargs: Dict[str, Any]) -> ModifiedAccessConditions: ...
def get_source_conditions(kwargs: Dict[str, Any]) -> SourceModifiedAccessConditions: ...
def get_cpk_scope_info(kwargs: Dict[str, Any]) -> CpkScopeInfo: ...
def get_container_cpk_scope_info(kwargs: Dict[str, Any]) -> ContainerCpkScopeInfo: ...
def get_api_version(kwargs: Any, default: Any): ...
