import pytest


def test_true() -> None:
    assert True


def test_raise() -> None:
    with pytest.raises(Exception):
        raise
