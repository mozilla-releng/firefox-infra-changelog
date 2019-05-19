from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Logger import FICLogger
import json


class FICCore(FICGithub, FICMercurial, FICFileHandler, FICLogger):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICFileHandler.__init__(self)
        FICLogger.__init__(self)
        self.check_tool_integrity()

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, days=3):
        # Don't forget about days!
        if all:
            for hosting_service in json.load(self.load(None, "repositories.json")):
                for repo in json.load(self.load(None, "repositories.json")).get(hosting_service):
                    self.repo_name = repo
                    self.start_git() if hosting_service == "Github" else self.start_hg()

        if git_only:
            for repo in json.load(self.load(None, "repositories.json")).get("Github"):
                self.repo_name = repo
                self.start_git()

        if hg_only:
            for repo in json.load(self.load(None, "repositories.json")).get("HG"):
                self.repo_name = repo
                self.start_hg()

        if repo_list:
            for repo in repo_list:
                self.repo_name = repo
                try:
                    self.start_git()
                except TypeError:
                    self.start_hg()

    def _markdown(self):
        self.git_markdown()
        self.hg_markdown()
        self.main_markdown()


