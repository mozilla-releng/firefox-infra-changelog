from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Logger import FICLogger


class FICCore(FICGithub, FICMercurial, FICFileHandler, FICLogger):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICFileHandler.__init__(self)
        FICLogger.__init__(self)

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, days=3):
        # Don't forget about days!

        if all:
            pass

        if git_only:
            pass

        if hg_only:
            pass

        if repo_list:
            pass

    def _markdown(self):
        pass

