import logging

from fastapi import FastAPI

from pkgtest import services
from pkgtest.config import Settings, settings
from pkgtest.model import HealthCheck

log = logging.getLogger(__name__)
app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Hello World"


@app.get("/health")
def get_health() -> HealthCheck:
    return services.health_check()


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


@app.get("/add")
async def add(a: int, b: int) -> int:
    res = services.add(a, b)
    log.info(res)
    return res


@app.get("/sub")
async def sub(a: int, b: int) -> int:
    res = services.sub(a, b)
    log.info(res)
    return res


@app.get("/cadd")
async def cadd(a: int, b: int) -> int:
    res = services.cadd(a, b)
    log.info(res)
    return res
