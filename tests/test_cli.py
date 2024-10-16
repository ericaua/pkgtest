from typer.testing import CliRunner

from pkgtest.cli import app

runner = CliRunner()


def test_root() -> None:
    res = runner.invoke(app, ["/"])
    assert res.exit_code == 0
    assert "Hello World" in res.stdout


def test_hello() -> None:
    name = "asdf"
    res = runner.invoke(app, ["hello", name])
    assert res.exit_code == 0
    assert f"Hello {name}" in res.stdout
    res = runner.invoke(app, ["hi", name])
    assert res.exit_code == 0
    assert f"Hello {name}" in res.stdout


def test_goodbye() -> None:
    name = "asdf"
    res = runner.invoke(app, ["goodbye", name])
    assert res.exit_code == 0
    assert f"Goodbye {name}" in res.stdout
    res = runner.invoke(app, ["bye", name])
    assert res.exit_code == 0
    assert f"Goodbye {name}" in res.stdout


def test_config() -> None:
    res = runner.invoke(app, ["config"])
    assert res.exit_code == 0
    assert "Settings(name" in res.stdout


def test_add() -> None:
    a, b = 17, 42
    res = runner.invoke(app, ["add", f"{a}", f"{b}"])
    assert res.exit_code == 0
    assert f"{a+b}" in res.stdout
