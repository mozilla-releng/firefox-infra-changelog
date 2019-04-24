from modules.FIC_DataVault import FICDataVault
from modules.config import COMMIT_DESCRIPTION_LENGTH
from modules.FIC_Logger import FICLogger


class FICFilters(FICDataVault, FICLogger):
    def __init__(self):
        FICDataVault.__init__(self)
        FICLogger.__init__(self)

    def trim_commit_description(self, commit_link, length=COMMIT_DESCRIPTION_LENGTH):
        if len(self.commit_message) > length:
            self.commit_message = self.commit_message[0:length] + ".. [continue reading](" + commit_link + ")"
        return self.commit_message

