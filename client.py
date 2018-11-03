import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import requests
import json

# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)


def create_git_link(project):
    """
    Expects the name of a project as a parameter and creates the api link for the json.
    We know 'services' is the only project in the mozilla repo while the rest are in mozilla-releng
    :param project:
    :return: GitHub Api link
    """
    beginning_url = "https://api.github.com/repos/"
    end_url = "/commits"
    if project == "release-services":
        git_url = beginning_url + "mozilla/" + project + end_url
    else:
        git_url = beginning_url + "mozilla-releng/" + project + end_url
    return git_url


def get_commits(link):
    """
    Makes the json request and return the request result as a list.
    :param link:
    :return: json list
    """
    commits_response = requests.get(link)
    commits_result = commits_response.json()
    return commits_result


def write_commits(commit_content, file_name):
    """
    Writes commit content to a provided file.
    :param commit_content:
    :param file_name:
    :return: none
    """
    with open(file_name, "w") as json_file:
        json.dump(commit_content, json_file, indent=2)


def filter_commit_data(commit):
    """
    Filters out only the data that we need from a commit
    :param commit_data:
    :return: filtered json data
    """
    repo_dict = {}
    number = 1
    for item in commit:
        each_commit = {}
        author_info = {}
        author_info.update({'sha': item['sha'],
                            'url': item['url'],
                            'author_info': item['commit']['author'],
                            'commit_message': item['commit']['message']})
        each_commit.update({number: author_info})
        number += 1
        repo_dict.update(each_commit)
    return repo_dict


# Get Name of Repositories of user.
# Then print only first 2 results.
# for repo in git.get_user().get_repos()[:2]:
#     print(repo.name)

# Get Commits in a Repository and print the author.
# Print last 5 committer names.
# for commit in git.get_user().get_repo("taskcluster-worker-checker").get_commits()[:5]:
#     print(commit.author.login)
#
# # Get Commits only made in the last 3 days!
# last_3days = datetime.now() - timedelta(days=3)
# repo = git.get_user().get_repo("taskcluster-worker-checker").get_commits(since=last_3days)
# for data in repo:
#     print(data.commit.author.name)
#     print(data.commit.message)


if __name__ == "__main__":
    user = git.get_user()  # Get Name of user.
    print(user.name + " is asking: ")
    project = input("What to search? : ")
    commit_data = get_commits(create_git_link(str(project)))
    useful_data = filter_commit_data(commit_data)
    write_commits(useful_data, "changelog.json")
