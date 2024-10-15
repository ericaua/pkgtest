import logging

from fastapi import FastAPI

from pkgtest import services
from pkgtest.config import Settings, settings

log = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Hello World"


@app.get("/hello")
@app.get("/hi")
async def hello(name: str) -> str:
    res = services.hello(name)
    log.info(res)
    return res


@app.get("/goodbye")
@app.get("/bye")
async def goodbye(name: str) -> str:
    res = services.goodbye(name)
    log.info(res)
    return res


@app.get("/config")
async def config() -> Settings:
    res = settings
    log.info(res)
    return res
