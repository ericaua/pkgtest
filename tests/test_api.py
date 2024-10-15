from fastapi.testclient import TestClient

from pkgtest.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"


def test_hello():
    name = "asdf"
    response = client.get(f"/hello?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Hello {name}!"
    response = client.get(f"/hi?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Hello {name}!"


def test_goodbye():
    name = "asdf"
    response = client.get(f"/goodbye?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Goodbye {name}!"
    response = client.get(f"/bye?name={name}")
    assert response.status_code == 200
    assert response.json() == f"Goodbye {name}!"


def test_config():
    response = client.get("/config")
    assert response.status_code == 200
