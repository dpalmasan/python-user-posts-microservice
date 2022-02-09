import yaml
from pydantic.dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    db_uri: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str

    @classmethod
    def load_from_file(cls, path: Path) -> "Config":
        with open(path, "r") as stream:
            cfg = yaml.safe_load(stream)
        return cls(**cfg["db"])
