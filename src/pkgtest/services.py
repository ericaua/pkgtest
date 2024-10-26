from pkgtest.model import HealthCheck


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
