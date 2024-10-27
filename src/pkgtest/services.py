from ctypes import cdll
from typing import cast

from pkgtest.model import HealthCheck

dll = cdll.LoadLibrary(name="./src/c/cadd.so")


def hello(name: str) -> str:
    return f"Hello {name}!"


def health_check() -> HealthCheck:
    return HealthCheck(status="OK")


def goodbye(name: str) -> str:
    return f"Goodbye {name}!"


def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def cadd(a: int, b: int) -> int:
    return cast(int, dll.cadd(a, b))
