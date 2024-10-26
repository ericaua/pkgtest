from dataclasses import dataclass


@dataclass
class HealthCheck:
    status: str = "OK"
