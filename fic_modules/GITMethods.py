from git import Repo


class FICGithub:
    def __init__(self, files, msg, LOGGER, config):
        self.files = files
        self.msg = msg
        self.LOGGER = LOGGER
        self.config = config

    def git_add(self):
        try:
            repo = Repo(self.config)
            for file in self.files:
                repo.git.add(file, update=True)
                if not repo.index.diff("HEAD"):
                    self.LOGGER.info("nothing staged for commit. has the data or files changed?")
        except:
            self.LOGGER.info("Failed to add the files")

    def git_commit(self):
        self.LOGGER.info("Committing changes with message: %s", self.msg)
        repo = Repo(self.config)
        commit = repo.index.commit(self.msg)
        for patch in repo.commit("HEAD~1").diff(commit, create_patch=True):
            self.LOGGER.info(patch)

    def git_push(self):
        try:
            repo = Repo(self.config)
            self.LOGGER.info("pushing changes to %s", repo)
            push_info = repo.remotes.origin.push(refspec=repo.active_branch)
            self.LOGGER.info("Summary of push: {}".format(push_info[0].summary))
        except:
            self.LOGGER.info("Error pushing the dates")
        finally:
            self.LOGGER.info("Data push from {} succeeded".format("Firefox Infra Changelog"))

    def git_pull(self):
        try:
            repo = Repo(self.config)
            self.LOGGER.info("pulling changes from %s", repo)
            pull_info = repo.remotes.origin.pull(refspec=repo.active_branch)
            self.LOGGER.info("Summary of pull: {}".format(pull_info[0]))
        except:
            self.LOGGER.info("Error pulling the dates")
        finally:
            self.LOGGER.info("Data pull from {} succeeded".format("Firefox Infra Changelog"))
