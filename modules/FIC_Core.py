import json

from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_Logger import FICLogger
from plugins.FIC_Markdown import FICMarkdownGenerator
from modules.config import CHANGELOG_REPO_PATH, CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, DEFAULT_DAYS, REPOSITORIES_FILE
from modules.FIC_Utilities import return_time


class FICCore(FICGithub, FICMercurial, FICMarkdownGenerator, FICLogger):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICMarkdownGenerator.__init__(self)
        FICLogger.__init__(self)
        self.check_tool_integrity()

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, push=False, days=DEFAULT_DAYS, logging=False):
        """
        The main method that runs the script depending on the following parameters.
        :param all: runs script for all available repositories
        :param git_only: runs script only for repositories that are on GitHub
        :param hg_only: runs script only for repositories that are on Mercurial
        :param repo_list: runs script for the repositories chosen by user
        :param days: generate the main markdown table (changelog.md) for <int> amount of days
        :param logging: activate the logger output in the console
        :param push: auto push the changes to GitHub
        """
        if logging:
            self.console_logging()

        if all:
            self.LOGGER.debug("Run all behavior mode")
            self._run_all_behavior()

        if git_only:
            self.LOGGER.debug("Run Github mode")
            self._run_git_behavior()

        if hg_only:
            self.LOGGER.debug("Run Mercurial mode")
            self._run_hg_behavior()

        if repo_list:
            self.LOGGER.debug("Run repo list mode")
            self._run_custom_repos_behavior(repo_list)

        self.populate_changelog_json(days)
        self.create_changelog_md()

        if push:
            self.push_to_git()

    def _run_all_behavior(self):
        """
        This method runs script for all available repositories
        """
        # Describes the behavioral of the script that runs in all mode.
        for hosting_service in json.load(self.load(None, REPOSITORIES_FILE)):
            for repo in json.load(self.load(None, REPOSITORIES_FILE)).get(hosting_service):
                self.LOGGER.debug(f"{hosting_service} working on repo: {repo}")
                if hosting_service == "Github":
                    self.start_git(repo)
                    self.start_md_for_git(repo)
                else:
                    self.start_hg(repo)
                    self.start_md_for_hg(repo)

    def _run_git_behavior(self):
        """
        This method runs script only for repositories that are on GitHub
        """
        # Describes the behavioral of the script that runs in git only mode.
        for repo in json.load(self.load(None, REPOSITORIES_FILE)).get("Github"):
            self.LOGGER.debug(f"Github: Working on repo: {repo}")
            self.start_git(repo)
            self.start_md_for_git(repo)

    def _run_hg_behavior(self):
        """
        This method runs script only for repositories that are on Mercurial
        """
        # Describes the behavioral of the script that runs in hg only mode.
        for repo in json.load(self.load(None, REPOSITORIES_FILE)).get("Mercurial"):
            self.LOGGER.debug(f"Mercurial: Working on repo: {repo}")
            self.start_hg(repo)
            self.start_md_for_hg(repo)

    def _run_custom_repos_behavior(self, user_repos):
        """
        This method runs script only for repositories chosen by user
        :param user_repos:  list of repositories chosen by user
        """
        # Describes the behavioral of the script that runs with custom repos mode.
        for repo in user_repos:
            self.LOGGER.debug(f"{repo[1]} working on repo: {repo[0]}")
            if repo[1] == "Github":
                self.start_git(repo[0])
                self.start_md_for_git(repo[0])
            elif repo[1] == "Mercurial":
                self.start_hg(repo[0])
                self.start_md_for_hg(repo[0])
            else:
                self.LOGGER.critical(f"Unknown repository type. Got {repo[1]} but can only accept 'Github' or 'Mercurial'")
                exit(12)

    def _extract_git_commits(self, key, changelog, number_of_days):
        """
        The method to extract the commits from GitHub repositories for <int> amount of days.
        :param key: repository name
        :param changelog: the dictionary of commits for changelog.json
        :param number_of_days: the amount of days to extract the commits
        """
        repo_data = json.load(self.load(CHANGELOG_REPO_PATH, key.lower() + ".json"))
        if len(repo_data) > 0:
            repo_data.pop("0")
            changelog["Github"].update({key: {}})
            commit_number = 0
            for value in repo_data.values():
                time_span = return_time(output_time_format="%Y-%m-%dT%H:%M:%S.%f", operation="sub", operation_days=number_of_days)
                if return_time(input_time=value["date"], input_time_format="%Y-%m-%dT%H:%M:%SZ") > time_span:
                    changelog["Github"][key].update({commit_number: value})
                    commit_number += 1

    def _extract_hg_commits(self, key, changelog, number_of_days):
        """
        The method to extract the commits from Mercurial repositories for <int> amount of days.
        :param key: repository name
        :param changelog: the dictionary of commits for changelog.json
        :param number_of_days: the amount of days to extract the commits
        """
        repo_data = json.load(self.load(CHANGELOG_REPO_PATH, key.lower() + ".json"))
        if len(repo_data) > 0:
            repo_data.pop("0")
            changelog["Mercurial"].update({key: {}})
            commit_number = 0
            for value in repo_data.values():
                time_span = return_time(output_time_format="%Y-%m-%dT%H:%M:%S.%f", operation="sub", operation_days=number_of_days)
                if return_time(input_time=value["date_of_push"], input_time_format="%Y-%m-%dT%H:%M:%S.%f") > time_span:
                    changelog["Mercurial"][key].update({commit_number: value})
                    commit_number += 1

    def populate_changelog_json(self, number_of_days):
        """
        This method generate changelog.json for <int> amount of days
        :param number_of_days: the amount of days to extract the commits
        """
        changelog = {}
        changelog.update({"Github": {},
                          "Mercurial": {}})
        with open(self.construct_path(None, REPOSITORIES_FILE), "r") as json_data:
            local_data = json.load(json_data)
            # Check all Github files exist for each repository.
            for key in local_data["Github"].keys():
                self._extract_git_commits(key, changelog, number_of_days)
            for key in local_data["Mercurial"].keys():
                self._extract_hg_commits(key, changelog, number_of_days)
        self.save(None, CHANGELOG_JSON_PATH, changelog)
        self.LOGGER.debug(f"changelog.json has been updated")
