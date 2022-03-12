from config import Config
from pymongo import MongoClient
import logging


def create_db_session(config: Config) -> MongoClient:
    client = MongoClient(host=config.db_uri, port=config.db_port)
    logging.info(
        f"Creating Mongo client host: {config.db_uri} port: {config.db_port}"
    )
    return client[config.db_name]
