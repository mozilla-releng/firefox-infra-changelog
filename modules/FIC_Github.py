# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_DataVault import FICDataVault
from modules.config import *
from modules.FIC_Utilities import return_time
from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH, INDIVIDUAL_REPO_DAYS
from git import Repo
import os
import json
import requests
import re


class FICGithub(FICFileHandler, FICDataVault):
    """
    This class handles the extracting, filtering and writing data into json file for git repos
    that affect firefox infra
    """
    def __init__(self):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.token_counter = 0
        self._get_os_var()
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.repo_data = None
        self.repo = Repo(self.construct_path(None, None))

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self):
        """
        It calls the method that gets all the repository data, using it's name, team and the authentication credential
        as parameters.
        """
        return self._init_github(self._gh, self.team_name, self.repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def _get_os_var(self):
        for var in os.environ:
            # append the OS.VAR to the list in case of no duplicate
            if "GIT_TOKEN" in var and var not in GIT_TOKEN:
                GIT_TOKEN.append(var)
        self.LOGGER.info(f"The list of available tokens: {GIT_TOKEN}")

    def _get_reset_time(self):
        reset_time = return_time(input_time=self._gh.rate_limit()['rate']['reset'], input_time_unix=True)
        self.LOGGER.info(f"Rate limit reset in: {reset_time - return_time()}")
        return reset_time

    def limit_checker(self):
        """Checks for the amount of limit requests remaining on a specific token.
        Switches to a new token from a group of defined tokens upon reaching 5 requests remaining
        """
        limit_requests = self._gh.ratelimit_remaining
        self.LOGGER.info(f"The number of limit requests is: {limit_requests}")
        if limit_requests < 5 and len(GIT_TOKEN) > 1:
            # switch token
            if self._switch_token():
                return True
            else:
                # check if the rate limit was reset for the second use of a token
                if limit_requests < 5:
                    self._get_reset_time()
                    return False
                else:
                    return True
        # check the reset time in case of a single token
        elif limit_requests < 5:
            self._get_reset_time()
            return False
        # return True in case of limit request not reached
        else:
            return True

    def _switch_token(self):
        """
        Method that switches git tokens
        """
        # get next token
        switch = self._get_token()
        # re-logging with the new token
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.LOGGER.info("The token was changed.")
        return switch

    def _get_token(self):
        """
        Returns the next token from the list of defined tokens
        """
        # in case of the next token but not the last
        if self.token_counter < len(GIT_TOKEN) - 1:
            self.token_counter += 1
            self.LOGGER.info(f"Changing token with: {GIT_TOKEN[self.token_counter]}")
            return True
        # in case of the last token
        elif self.token_counter == len(GIT_TOKEN) - 1:
            self.token_counter = 0
            self.LOGGER.info(f"Changing token with: {GIT_TOKEN[self.token_counter]}")
            return False

    def pull(self):
        """
        Pulls changes for a git repo
        :return: the pulled changes
        """
        self.LOGGER.info(f"pulling changes from {self.repo.remotes.origin.url} -> Branch {self.repo.active_branch}")
        return self.repo.remotes.origin.pull(refspec=self.repo.active_branch)

    def add(self):
        """
        Adds modified files that will be commited
        :return: True or False, depending if there are changes
        """
        self.repo.git.add([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH], update=True)
        return self.check_for_changes()

    def check_for_changes(self):
        """
        Checkes if there are any important changes regarding infra-tracking
        :return: True or False, depending if there are changes
        """
        if not self.repo.index.diff("HEAD"):
            self.LOGGER.info("Nothing staged for commit. has the data or files changed?")
            return False
        return True

    def commit(self):
        """
        Commits the added changes
        """
        self.LOGGER.info(f"Committing changes with message: Changelog: {return_time()}")
        return self.repo.index.commit("Changelog: " + return_time(output_time_format="%Y-%m-%dT%H:%M:%S"))

    def push_to_git(self):
        """
        Pushes the commited changes to github
        """
        self.LOGGER.info(f"Summary of pull: {FICGithub.pull(self)[0]}")
        if FICGithub.add(self):
            self.LOGGER.info(f"Summary of commit {FICGithub.commit(self)}")
            self.LOGGER.info(f"pushing changes to {self.repo.remotes.origin.url}  on branch  {self.repo.active_branch}")
            self.LOGGER.info(f"Summary of push: {self.repo.remotes.origin.push(refspec=self.repo.active_branch)[0].summary}")

    def revert_modified_files(self):
        """
        Undo any changes to files in case the script fails to run successfully
        """
        return self.repo.git.checkout([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH])

    def get_repo_url(self):
        """
        It gets the repository URL.
        :return: the URL of the repository
        """
        return self.repo_data.svn_url

    def _repo_team(self):
        self.team_name = json.load(self.load(None, REPOSITORIES_FILE)).get("Github").get(self.repo_name).get("team")

    def _repo_files(self):
        self.folders_to_check = json.load(self.load(None, REPOSITORIES_FILE)).get("Github").get(self.repo_name).get("configuration").get("folders-to-check")

    def _extract_repo_type(self):
        self.repo_type = json.load(self.load(None, REPOSITORIES_FILE)).get("Github").get(self.repo_name).get("configuration").get("type")

    def _local_version(self):
        if json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0"):
            self.local_version = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0").get("version")

    def _get_release(self, release_number):
        return [tag for tag in self.repo_data.tags(number=release_number)][release_number - 1].name

    def _get_version_path(self):
        self.version_path = json.load(self.load(None, REPOSITORIES_FILE)).get("Github").get(self.repo_name).get("configuration").get("version-path")

    def _build_puppet_version(self):
        self._get_version_path()
        for requirements in requests.get(self.version_path).text.split():
            if self.repo_name in requirements:
                self.build_puppet_version = re.split("\\b==\\b", requirements)[-1]
                return True

    def _compare_versions(self):
        """
        Checks the latest version of a repo locally, on github and in build-puppet if defined
        :return: True if the checked places return different version, otherwise False
        """
        if self.build_puppet_version == self.release_version and self.release_version != self.local_version:
            return True
        else:
            return False

    def _last_checked(self):
        """
        :return: the last checked value in the json files. If there isn't one use DEFAULT_DAYS
        """
        if json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0"):
            self.last_check = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0").get("last_checked")
        else:
            self.last_check = return_time(output_time_format="%Y-%m-%dT%H:%M:%S.%f", operation="sub", operation_days=DEFAULT_DAYS)

    def _commit_iterator(self):
        """
        Iterates through the commits of a repo and save it if contains infra changes
        """
        for current_commit in self.repo_data.commits(since=self.last_check):
            if self.limit_checker():
                self._get_message(current_commit)
                self._get_sha(current_commit)
                self._get_files()
                if self._commit_filter():
                    self.commit_number += 1
                    self._store_data(current_commit)
                    self._construct_commit()
        self.keyword = None

    def _store_data(self, current_commit):
        """
        extracts the data we care about from a commit object
        """
        self._get_date(current_commit)
        self._get_author(current_commit)
        self._get_author_email(current_commit)
        self._get_url(current_commit)

    def _get_sha(self, commit):
        self.commit_sha = commit.sha
        return self.commit_sha

    def _get_message(self, commit):
        self.commit_message = commit.message
        return self.commit_message

    def _get_date(self, commit):
        self.commit_date = commit.commit.author.get("date")
        return self.commit_date

    def _get_author(self, commit):
        self.commit_author = commit.commit.author.get("name")
        return self.commit_author

    def _get_author_email(self, commit):
        self.commit_author_email = commit.commit.author.get("email")
        return self.commit_author_email

    def _get_url(self, commit):
        self.commit_url = commit.url
        return self.commit_url

    def _get_files(self):
        self.commit_files_changed = []
        for item in (range(len(self.repo_data.commit(sha=self.commit_sha).files))):
            self.commit_files_changed.append(self.repo_data.commit(sha=self.commit_sha).files[item].get('filename'))

    def _compare_files(self):
        """
        Checks to see if any of the files we track in a repo were changed
        :return: True if any of the files we care about received changes
        """
        for folder_to_check in range(len(self.folders_to_check)):
            for changed_folder in range(len(self.commit_files_changed)):
                if str(self.folders_to_check[folder_to_check]) in str(self.commit_files_changed[changed_folder]):
                    return True

    def _construct_commit(self):
        """
        Constructs the object that stores all the data we care about for a single commit
        """
        self.list_of_commits.update({self.commit_number: {'sha': self.commit_sha,
                                                          'url': self.commit_url,
                                                          'author': self.commit_author,
                                                          'author_email': self.commit_author_email,
                                                          'message': self.commit_message,
                                                          'date': self.commit_date,
                                                          'files': f"This commit contains {len(self.commit_files_changed)} files changed."
                                                          }
                                     })

    def _commit_filter(self):
        """
        Determines if we care about saving a commit
        :return: True if the repo type and its conditions are met
        """
        if self.repo_type == "commit-keyword":
            if self.keyword in self.commit_message:
                return True

        elif self.repo_type == "tag":
            if self.repo_name == "build-puppet":
                return True

            elif self.release_version in self.commit_message:
                return True

        elif len(self.folders_to_check) > 0:
            if self._compare_files():
                return True

        else:
            return True

    def _not_tag(self):
        self._last_checked()
        self._commit_iterator()

    def _build_puppet(self):
        self._last_checked()
        self._commit_iterator()

    def _tag(self):
        self._last_checked()
        self.release_version = self._get_release(1)
        self._local_version()
        if self.repo_name == "mozapkpublisher" and self.release_version != self.local_version:
            self._commit_iterator()
        else:
            self._build_puppet_version()
            if self._compare_versions():
                self._commit_iterator()

    def _commit_keyword(self):
        self._last_checked()
        self.keyword = 'deploy'
        self._commit_iterator()

    def _repo_type_checker(self):
        """
        Checks the type of a repo, as defined in repositories.json, and runs the appropriate methods
        """
        if self.repo_type == "no-tag":
            self._not_tag()

        elif self.repo_type == "tag":
            if self.repo_name == "build-puppet":
                self._build_puppet()
            else:
                self._tag()

        elif self.repo_type == "commit-keyword":
            self._commit_keyword()
        else:
            self.LOGGER.critical(f"Repo type not defined for {self.repo_name}")

    def _generate_first_element(self):
        """
        Creates the first element which will be at the top of the json file
        :return:
        """
        if self.repo_type == "tag" and self.repo_name != "build-puppet":
            return {"0": {"last_checked": return_time(output_time_format="%Y-%m-%dT%H:%M:%S.%f"), "version": self._get_release(1)}}
        else:
            return {"0": {"last_checked": return_time(output_time_format="%Y-%m-%dT%H:%M:%S.%f")}}

    def start_git(self, repo_name=None):
        """
        The entry point for git. Runs the entire logic for a one git repo at a time
        :param repo_name: name of the git repo to be worked on
        """
        self.list_of_commits = {}
        self.repo_name = repo_name
        self._extract_repo_type()
        self._repo_team()
        self.read_repo()
        self._repo_files()
        self.commit_number = 0
        self.list_of_commits.update(self._generate_first_element())
        self._repo_type_checker()
        self._write_git_json()

    def _check_commit_age(self, filter_list=None):
        """
        Removes data that is older tham a set amount of days. Default = 30
        :param filter_list: awaits a list of commit data
        """
        for commit in range(1, len(filter_list)):
            if return_time(input_time=filter_list[str(commit)]["date"], input_time_format="%Y-%m-%dT%H:%M:%SZ") > \
               return_time(operation="sub", operation_days=INDIVIDUAL_REPO_DAYS):
                self.commit_number += 1
                self.list_of_commits.update({str(self.commit_number): filter_list[str(commit)]})

    def _write_git_json(self):
        """
        Writes the final, filtered, extracted data to json files
        """
        local_json_data = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json"))
        # In case we have no new commits to save
        if len(self.list_of_commits) == 1:
            local_json_data.update(self._generate_first_element())
            self._check_commit_age(local_json_data)
            self.save(CHANGELOG_REPO_PATH, self.repo_name + ".json", self.list_of_commits)
        # In case we have new commits + local data
        elif len(local_json_data) >= 1:
            local_json_data.pop("0")
            self._check_commit_age(local_json_data)
            self.save(CHANGELOG_REPO_PATH, self.repo_name + ".json", self.list_of_commits)
        # In case we have new commits and NO local data
        else:
            self.save(CHANGELOG_REPO_PATH, self.repo_name + ".json", self.list_of_commits)
