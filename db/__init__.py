import logging
import os
from pathlib import Path

from config import Config
from db.session import create_db_session

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

cwd = os.getcwd()
logger.info(f"Working directory {cwd}")
logger.info(f"Files {os.listdir(os.path.join(cwd, 'app_config'))}")
config_file = Path("app_config/config.yaml")
if not config_file.exists():
    logger.info("No app_config/config.yaml was found ")
    config_file = Path("app_config/config.default.yaml")

logger.info(f"Using {config_file}")
config = Config.load_from_file(config_file)
session = create_db_session(config)
