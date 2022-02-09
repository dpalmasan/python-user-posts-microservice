from config import Config
from db.session import create_db_session

config = Config.load_from_file("config.yaml")
session = create_db_session(config)
