import logging

from pymongo import MongoClient

from config import Config


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# add formatter to ch
ch.setFormatter(formatter)

logger.addHandler(ch)


def create_db_session(config: Config) -> MongoClient:
    client = MongoClient(host=config.db_uri, port=config.db_port)
    logger.info(
        f"Creating Mongo client host: {config.db_uri} port: {config.db_port}"
    )
    return client[config.db_name]
