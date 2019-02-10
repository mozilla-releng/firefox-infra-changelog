import subprocess
import datetime

subprocess.call(['git', 'checkout', 'auto-generated-files'])
subprocess.call(['git', 'add', 'git_files/*'])
subprocess.call(['git', 'add', 'hg_files/*'])
subprocess.call(['git', 'add', 'main_md_table.md'])
commit_message = "Changelog:  " + str(datetime.datetime.now()) + \
                    "\n - updated git files \n - updated hg files \n - updated main_md_table"
subprocess.call(['git', 'commit', '-m', commit_message])
subprocess.call(['git', 'push', 'origin', 'auto-generated-files'])
