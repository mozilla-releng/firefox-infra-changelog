# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3


class FICGithub:
    def __init__(self):
        from modules.config import GIT_TOKEN
        import os
        self._token = os.environ.get(GIT_TOKEN)
        self._gh = self._auth()
        self.repo_data = None

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self, team_name, repo_name):
        return self._init_github(self._gh, team_name, repo_name)

    def _init_github(self, session, *args):
        self.repo_data = github3.GitHub.repository(session, args[0], args[1])
        return self.repo_data
