import re
from git import Repo
import subprocess
from fic_modules.configuration import LOGGER
from datetime import datetime


def git_add(files, LOGGER, config="./"):
    try:
        repo = Repo(config)
        for file in files:
            repo.git.add(file, update=True)
            if not repo.index.diff("HEAD"):
                LOGGER.info("nothing staged for commit. has the data or files changed?")
    except:
        LOGGER.info("Failed to add the files")


def git_commit(msg, LOGGER, config="."):
    LOGGER.info("Committing changes with message: %s", msg)
    repo = Repo(config)
    commit = repo.index.commit(msg)
    for patch in repo.commit("HEAD~1").diff(commit, create_patch=True):
        LOGGER.info(patch)


def git_push(LOGGER, config="."):
    try:
        repo = Repo(config)
        LOGGER.info("pushing changes to %s", repo)
        push_info = repo.remotes.origin.push(refspec='master')
        LOGGER.info("Summary of push: {}".format(push_info[0].summary))
    except:
        LOGGER.info("Error pushing the dates")
    finally:
        LOGGER.info("Data push from {} succeeded".format("Firefox Infra Changelog"))


def git_pull(LOGGER, config='.'):
    repo = Repo(config)
    LOGGER.info("pulling changes from %s", repo)
    pull_info = repo.remotes.origin.pull(refspec='master')
    LOGGER.info("Summary of push: {}".format(pull_info[0]))


git_pull(LOGGER)
subprocess.call(['python', 'client.py', '-c', '-l'])
commit_message = "Changelog: " + str(datetime.utcnow())
files = ["git_files", "hg_files", "changelog.json", "changelog.md"]
git_add(files, LOGGER)
git_commit(commit_message, LOGGER)
git_push(LOGGER)
