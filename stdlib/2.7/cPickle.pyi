from typing import Any, IO, List

HIGHEST_PROTOCOL = ...  # type: int
compatible_formats = ...  # type: List[str]
format_version = ...  # type: str

class Pickler:
    def __init__(self, file: IO[str], protocol: int = ...) -> None: ...


class Unpickler:
    def __init__(self, file: IO[str]) -> None: ...

def dump(obj: Any, file: IO[str], protocol: int = ...) -> None: ...
def dumps(obj: Any, protocol: int = ...) -> str: ...
def load(file: IO[str]) -> Any: ...
def loads(str: str) -> Any: ...

class PickleError(Exception): ...
class UnpicklingError(PickleError): ...
class BadPickleGet(UnpicklingError): ...
class PicklingError(PickleError): ...
class UnpickleableError(PicklingError): ...
