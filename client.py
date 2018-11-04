import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import requests
import json

# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)


def hg_timestamps_handler(timestamp, timezone):
    """
    This function handles the mercurial timestamps so that all of the modifications to be traceable in time, in
    concordance to one
    another and returns the date-time format.
    Part of Mercurial Wrapper
    Example :
        print(handle_timestamps("1499225169.0", "-43200"))
    Output:
        07-05-2017 15:26:09
    :param timestamp: Timestamp in unix systems (an unique time represented in how many seconds past a certain event)
    :param timezone: Timezone of the timestamp
    :return: Returns "YYYY-MM-DD HH:MM:SS"
    """
    if "-" in timezone:
        ts = int(timestamp[:-2]) - int(timezone)
    else:
        ts = int(timestamp[:-2]) + int(timezone)
    return datetime.utcfromtimestamp(ts).strftime("%m-%d-%Y %H:%M:%S")


def get_hg_changes(repository_name, push_type):
    """
    This function takes a repository and push type and returns a json object that contains changes in that specific
    repository.
    The HG API also supports xml and rss.

    Example:
    example = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    This will be later used to get the commits from https://hg.mozilla.org/

    :param repository_name: link of the repository, eg: https://hg.mozilla.org/build/nagios-tools/
    :param push_type: would probably be "json-log" most of the time.
    :return:
    """
    if push_type == "json-log":
        request_url = repository_name + push_type
        push_response = requests.get(request_url)
        hg_changes_result = push_response.json()
    else:
        print("Feature not implemented. Please use \"json-log\".")
    return hg_changes_result


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
    :param commit:
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
