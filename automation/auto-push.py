import subprocess
import datetime

subprocess.call(['git', 'add', '../tests/changelog.md'])
commit_message = "Changelog:  " + str(datetime.datetime.now())
subprocess.call(['git', 'commit', '-m', commit_message])
#subprocess.call(['git push'])