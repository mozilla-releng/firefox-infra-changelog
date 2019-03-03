import subprocess
from datetime import datetime
from win10toast import ToastNotifier
from fic_modules.configuration import LOGGER
toaster = ToastNotifier()
now = datetime.now()

branch_name = 'auto-push'
try:
    # Setup environment
    subprocess.call(['git', 'checkout', 'master'])
    subprocess.call(['git', 'pull'])
    subprocess.call(['git', 'branch', '-D', branch_name])
    subprocess.call(['git', 'checkout', '-b', branch_name])
    # Run FIC
    subprocess.call(['python', 'client.py', '-c', '-l'])
    # Prepare commit
    subprocess.call(['git', 'add', 'git_files/', 'hg_files/', 'LOG.log',
                     'changelog.md', 'changelog.json'])
    commit_message = "Changelog:  " + str(datetime.utcnow()) + \
                     "\n- updated git files \n- updated hg files" \
                     "\n- updated changelog.md \n- updated changelog.json"
    subprocess.call(['git', 'commit', '-m', commit_message])
    # Push commit to origin
    subprocess.call(['git', 'push', '--set-upstream', 'origin', branch_name])
    subprocess.call(['git', 'push'])
    toaster.show_toast("FireFox Infra Changelog",
                       "Generated files have been updated")
except Exception as e:
    toaster.show_toast("FireFox Infra Changelog",
                       "Failed to update the generated files")
    LOGGER.error(e)
