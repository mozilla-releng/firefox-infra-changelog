import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import json
import re
import requests
# Create a Github instance:
TOKEN = os.environ.get("GIT_TOKEN")
git = Github(TOKEN)
lastWeek = datetime.now() - timedelta(days=7)
current_dir = os.path.dirname(os.path.realpath(__file__))


def create_git_md_table(repository_name):
    """
    Uses 'project' and 'project_name' parameters to generate markdown tables for every json file inside 'git_files'.
    :param project: Project name
    :param project_name: used to display the repo name in the title row of the MD table
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/git_files/" + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = '| Commit Number | Comiter | Commit Message | Commit Url | Date | \n' + \
                     '|:---:|:----:|:----------------------------------:|:------:|:----:| \n'
        tables = {}
        md_title = ['{} commit markdown table since {}'.format(repository_name, lastWeek)]
        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            commiter = data[key]['commiter_name']
            date = data[key]['commit_date']
            message = data[key]['commit_message']
            url = data[key]['url']

            row = "|" + commit_number + \
                  "|" + commiter + \
                  "|" + message + \
                  "|" + "[URL](" + url + ")" + \
                  "|" + date + '\n'

            del commit_number_list[-1]
            for repo in tables.keys():
                tables[repo] = tables[repo] + row

        md_file_name = '{}.md'.format(repository_name)
        md_file = open(current_dir + "/git_files/" + md_file_name, 'w')

        for key, value in tables.items():
            if value != base_table:
                md_file.write('## ' + key.upper() + '\n\n')
                md_file.write(value + '\n\n')
        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!". format(repository_name))


def filter_commit_data(repository_name, repository_team):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param commit: json style content required to be filtered
    :return: filtered json data
    TODO: please add the exception blocks since the script fails when it can't pull a data:
    (e.g raise self.__createException(status, responseHeaders, output)
            github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    repo_dict = {}
    number = 1
    repository_path = repository_team + repository_name
    for commit in git.get_repo(repository_path).get_commits(since=lastWeek):
        each_commit = {}
        author_info = {}
        commit_sha = commit.sha
        commiter_name = commit.author.login
        commiter_email = commit.committer.email
        commit_message = commit.commit.message
        commit_html_url = commit.html_url
        commit_date = str(commit.commit.author.date)
        message = re.sub('[*\n\r]', ' ', commit_message)
        author_info.update({'sha': commit_sha,
                            'url': commit_html_url,
                            'commiter_name': commiter_name,
                            'commiter_email': commiter_email,
                            'commit_message': message,
                            'commit_date': commit_date
                            })
        each_commit.update({number: author_info})
        git_json_filename = "{}.json".format(repository_name)
        number += 1
        repo_dict.update(each_commit)
        json_file = open(current_dir + "/git_files/" + git_json_filename, 'w')
        json.dump(repo_dict, json_file, indent=2)
        json_file.close()


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
    :return: returns a json that contains the commits in the provided hg_repository_name
    """
    if push_type == "json-log":
        request_url = repository_name + push_type
        push_response = requests.get(request_url)
        hg_changes_result = push_response.json()
    else:
        print("Feature not implemented. Please use \"json-log\".")
    return hg_changes_result


def create_files_for_hg():
    """
    Main HG function. takes every Mercurial repo from repositories.json and writes all the commit data of each repo in a
    separate json file
    :return: the end result is a .json file for every HG repository. can be found inside hg_files/
    """
    for repo in repositories["Mercurial"]:
        repository_url = repositories["Mercurial"][repo]["url"]
        repository_push_type = repositories["Mercurial"][repo]["configuration"]["push_type"]
        repository_name = repositories["Mercurial"][repo]["name"]
        hg_changes = get_hg_changes(repository_url, repository_push_type)
        hg_json_name = "./hg_files/" + "{}.json".format(repository_name)
        with open(hg_json_name, "w") as json_file:
            json.dump(hg_changes, json_file, indent=2)
        json_file.close()

def create_files_for_git():
    """
    Main GIT function. Takes every Git repo from repositories.json and writes all the commit data of each repo in a
    separate json file and generates a MD file for each repo as well.
    :return: the end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories["Github"]:
        repository_name = repo
        repository_team = repositories["Github"][repo]["team"]
        filter_commit_data(repository_name, repository_team)
        create_git_md_table(repository_name)


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open('./repositories.json').read()
    repositories = json.loads(repositories_data)
    create_files_for_git()
    create_files_for_hg()

