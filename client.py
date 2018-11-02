import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta

# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)


# Get Name of user.
user = git.get_user()
print(user.name)


# Get Name of Repositories of user.
# Then print only first 2 results.
for repo in git.get_user().get_repos()[:2]:
    print(repo.name)


# Get Commits in a Repository and print the author.
# Print last 5 committer names.
for commit in git.get_user().get_repo("taskcluster-worker-checker").get_commits()[:5]:
    print(commit.author.login)


# Get Commits only made in the last 3 days!
last_3days = datetime.now() - timedelta(days=3)
repo = git.get_user().get_repo("taskcluster-worker-checker").get_commits(since=last_3days)
for data in repo:
    print(data.commit.author.name)
    print(data.commit.message)





