from fastapi.testclient import TestClient

from pkgtest.api import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_config() -> None:
    response = client.get("/config")
    assert response.status_code == 200


def test_hello() -> None:
    name = "asdf"
    response = client.get(f"/hello?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Hello {name}!"
    response = client.get(f"/hi?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Hello {name}!"


def test_goodbye() -> None:
    name = "asdf"
    response = client.get(f"/goodbye?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Goodbye {name}!"
    response = client.get(f"/bye?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Goodbye {name}!"


def test_add() -> None:
    a, b = 17, 42
    response = client.get(f"/add?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == a + b


def test_sub() -> None:
    a, b = 17, 42
    response = client.get(f"/sub?a={a}&b={b}")
    assert response.status_code == 200
    assert response.json() == a - b
