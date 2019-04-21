# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_Logger import FICLogger
from git import Repo


class FICGithub(FICLogger):
    def __init__(self):
        FICLogger.__init__(self)
        from modules.config import GIT_TOKEN
        import os
        self._token = os.environ.get(GIT_TOKEN)
        self._gh = self._auth()
        self.repo_data = None
        self.repo = Repo(".")

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self, team_name, repo_name):
        return self._init_github(self._gh, team_name, repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def pull(self):
        self.LOGGER.info("pulling changes from {} -> Branch {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
        return self.repo.remotes.origin.pull(refspec=self.repo.active_branch)

    def add(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        self.repo.git.add([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH], update=True)
        return self.check_for_changes()

    def revert_modified_files(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        return self.repo.git.checkout([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH])

    def check_for_changes(self):
        if not self.repo.index.diff("HEAD"):
            self.LOGGER.info("Nothing staged for commit. has the data or files changed?")
            return False
        return True

    def commit(self):
        from datetime import datetime
        self.LOGGER.info("Committing changes with message: Changelog: %s", str(datetime.utcnow()))
        return self.repo.index.commit("Changelog: " + str(datetime.utcnow()))

    def push(self):
        self.LOGGER.info("Summary of pull: {}".format(FICGithub.pull(self)[0]))
        if FICGithub.add(self):
            self.LOGGER.info("Summary of commit {}".format(FICGithub.commit(self)))
            self.LOGGER.info("pushing changes to {}  on branch  {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
            self.LOGGER.info("Summary of push: {}".format(self.repo.remotes.origin.push(refspec=self.repo.active_branch)[0].summary))
