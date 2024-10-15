import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)


@dataclass
class Settings:
    name: str = "Erik"


settings = Settings()
