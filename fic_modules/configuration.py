# FIC Configuration file
import os
import json
import logging
from github import Github
from datetime import (
    datetime,
    timedelta
)

REPOSITORIES_DATA = open("./repositories.json").read()
REPOSITORIES = json.loads(REPOSITORIES_DATA)
TOKEN = os.environ.get("GIT_TOKEN")
GIT = Github(TOKEN)
REPO_CHOICE = "ALL"
GENERATE_FOR_X_DAYS = int(1)
NUMBER_OF_CHANGESETS = int(100)
REPO_LIST = []
LAST_WEEK = datetime.now() - timedelta(days=14)
LAST_MONTH = datetime.utcnow() - timedelta(days=31)
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_DIR = CURRENT_DIR.strip("/fic_modules")

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)\
                    s:%(lineno)d] %(message)s",
                    datefmt="%H:%M:%S",
                    filename="LOG.log"
                    )
logger = logging.getLogger(__name__)


