import subprocess
from datetime import datetime
from win10toast import ToastNotifier
from fic_modules.configuration import LOGGER
toaster = ToastNotifier()
now = datetime.now()
branch_name = 'auto-generated-files-on-', str(now.strftime("%Y-%m-%d-%H-%M"))
try:
    subprocess.call(['git', 'checkout', '-b', branch_name])
    subprocess.call(['python', 'client.py', '-a', '-l'])
    subprocess.call(['git', 'add', 'git_files/', 'hg_files/', 'LOG.log',
                     'changelog.md'])
    commit_message = "Changelog:  " + str(datetime.utcnow()) + \
                     "\n - updated git files \n - updated hg files \n " \
                     "- updated main_md_table"
    subprocess.call(['git', 'commit', '-m', commit_message])
    subprocess.call(['git', 'push', '--set-upstream', 'origin', branch_name])
    subprocess.call(['git', 'push'])
    toaster.show_toast("FireFox Infra Changelog",
                       "Generated files have been updated")
except Exception as e:
    toaster.show_toast("FireFox Infra Changelog",
                       "Failed to update the generated files")
    LOGGER.error(e)
