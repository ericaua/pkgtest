import logging

import typer

from pkgtest import services
from pkgtest.config import settings

log = logging.getLogger(__name__)
app = typer.Typer()


@app.command("hello")
@app.command("hi")
def hello(name: str) -> None:
    res = services.hello(name)
    log.info(res)


@app.command("goodbye")
@app.command("bye")
def goodbye(name: str) -> None:
    res = services.goodbye(name)
    log.info(res)


@app.command()
def config() -> None:
    log.info(settings)
