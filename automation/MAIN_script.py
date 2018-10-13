import subprocess

#subprocess.call(['python', '../git-login.py'])
try:
	subprocess.call(['python', '../tests/git_api.py'])
	print("Git JSON is ready.")
	subprocess.call(['python', '../tests/hg_api.py'])
	print("Mercurial JSON is ready.")
	subprocess.call(['python', '../tests/json_changelog.py'])
	print("JSON changelog is ready")
	subprocess.call(['python', '../tests/md_changelog.py'])
	print("MD changelog is ready.")
	print("\nYour changelog is Up to Date")
except KeyboardInterrupt:
	exit(0)