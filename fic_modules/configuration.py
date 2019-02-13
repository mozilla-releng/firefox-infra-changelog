# FIC Configuration file
import os
import json
from github import Github
from datetime import (
    datetime,
    timedelta
)

LOGGER = False
REPOSITORIES_DATA = open("./repositories.json").read()
REPOSITORIES = json.loads(REPOSITORIES_DATA)
TOKEN = os.environ.get("GIT_TOKEN")
GIT = Github(TOKEN)
REPO_CHOICE = "ALL"
GENERATE_FOR_X_DAYS = int(1)
REPO_LIST = []
LAST_WEEK = datetime.now() - timedelta(days=14)
LAST_MONTH = datetime.utcnow() - timedelta(days=31)
CURRENT_DIR = r'C:/Users/roland.mutter/Desktop/FFCI/firefox-infra-changelog'