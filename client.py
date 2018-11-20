import os
from github import Github  # pip3 install PyGitHub
from datetime import datetime, timedelta
import json
import re
import requests
from os import listdir
from os.path import isfile, join

# Create a Github instance:
lastWeek = datetime.now() - timedelta(days=7)
current_dir = os.path.dirname(os.path.realpath(__file__))


def create_git_md_table(repository_name):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside 'git_files'.
    :param project: repository_name
    :param repository_name: used to display the repo name in the title row of the MD table
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/git_files/" + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = '| Commit Number | Commiter | Commit Message | Commit Url | Date | \n' + \
                     '|:---:|:----:|:----------------------------------:|:------:|:----:| \n'
        tables = {}
        md_title = ['{} commit markdown table since {}'.format(repository_name, lastWeek)]
        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            try:
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
            except KeyError:
                lastChecked = data[key]['lastChecked']

        md_file_name = '{}.md'.format(repository_name)
        md_file = open(current_dir + "/git_files/" + md_file_name, 'w')

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write('## ' + key.upper() + '\n\n')
                    md_file.write(value + '\n\n')
        except:
            pass

        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!". format(repository_name))


def create_hg_md_table(repository_name):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside 'hg_files'.
    :param project: repository_name
    :param repository_name: used to display the repo name in the title row of the MD table
    :return: MD tables for every json file inside the hg_files dir.
    """

    try:
        json_data = open(current_dir + "/hg_files/" + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = '| Commit Number | Commiter | Commit Message | Node | Date | \n' + \
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
            node = data[key]['node']

            row = "|" + commit_number + \
                    "|" + commiter + \
                    "|" + message + \
                    "|" + node + \
                    "|" + date + '\n'

            del commit_number_list[-1]
            for repo in tables.keys():
                tables[repo] = tables[repo] + row

        md_file_name = '{}.md'.format(repository_name)
        md_file = open(current_dir + "/hg_files/" + md_file_name, 'w')

        for key, value in tables.items():
            if value != base_table:
                md_file.write('## ' + key.upper() + '\n\n')
                md_file.write(value + '\n\n')
        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!".format(repository_name))


def filter_git_commit_data(repository_name, repository_team):
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
    number = 0
    repository_path = repository_team + repository_name
    print("Working on repo:", repository_name)
    repo_dict.update({number: {"lastChecked": str(datetime.utcnow())}})
    number += 1

    for commit in git.get_repo(repository_path).get_commits(since=lastWeek):
        each_commit = {}
        author_info = {}
        files_changed = []
        commit_sha = commit.sha
        commiter_name = commit.author.login
        commiter_email = commit.committer.email
        commit_message = commit.commit.message
        commit_html_url = commit.html_url
        for entry in commit.files:
            files_changed.append(entry.filename)
        commit_date = str(commit.commit.author.date)
        message = re.sub('[*\n\r]', ' ', commit_message)
        author_info.update({'sha': commit_sha,
                            'url': commit_html_url,
                            'commiter_name': commiter_name,
                            'commiter_email': commiter_email,
                            'commit_message': message,
                            'commit_date': commit_date,
                            'files_changed': files_changed
                            })
        each_commit.update({int(number): author_info})
        number += 1
        repo_dict.update(each_commit)

    git_json_filename = "{}.json".format(repository_name)
    json_file = open(current_dir + "/git_files/" + git_json_filename, 'w')
    json.dump(repo_dict, json_file, indent=2)
    json_file.close()


def filter_hg_commit_data(repository_url, push_type):
    """
    This function takes a repository url and push type and returns a dictionary that contains changes in that specific
    repository.
    The HG API also supports xml and rss.
    Example:
    example = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    This will be later used to get the commits from https://hg.mozilla.org/
    :param repository_url: link of the repository, eg: https://hg.mozilla.org/build/nagios-tools/
    :param push_type: would probably be "json-log" most of the time.
    :return: returns a dictionary that contains the commits in the provided hg_repository_name
    """
    if push_type == "json-log":
        request_url = repository_url + push_type
    else:
        print("Feature not implemented. Please use \"json-log\".")
    r = requests.get(request_url)
    p = r.json()
    changelog = {}
    commit_number = 0
    for keys in p['changesets']:
        commit = {}
        timestamp = keys['date'][0]
        value = datetime.fromtimestamp(timestamp)
        commit_date = value.strftime('%Y-%m-%d %H:%M:%S')
        commiter_name = (keys['user'])
        commit_message = keys['desc']
        message = re.sub('[*\n\r]', ' ', commit_message)
        commit_node = keys['node']
        commit.update({'commiter_name': commiter_name,
                        'commit_date': commit_date,
                        'commit_message': message,
                        'node': commit_node})
        changelog.update({commit_number: commit})
        commit_number += 1
    return changelog


def create_files_for_hg():
    """
    Main HG function. Takes every Mercurial repo from repositories.json and writes all the commit data of each repo in a
    separate json file and generates a MD file for each repo as well.
    :return: the end result is a .json and a .md file for every git repository. can be found inside hg_files/
    """
    for repo in repositories["Mercurial"]:
        repository_url = repositories["Mercurial"][repo]["url"]
        repository_push_type = repositories["Mercurial"][repo]["configuration"]["push_type"]
        repository_name = repo
        hg_changes = filter_hg_commit_data(repository_url, repository_push_type)
        hg_json_name = "./hg_files/" + "{}.json".format(repository_name)
        with open(hg_json_name, "w") as json_file:
            json.dump(hg_changes, json_file, indent=2)
        json_file.close()
        create_hg_md_table(repository_name)


def create_files_for_git():
    """
    Main GIT function. Takes every Git repo from repositories.json and writes all the commit data of each repo in a
    separate json file and generates a MD file for each repo as well.
    :return: the end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories["Github"]:
        repository_name = repo
        repository_team = repositories["Github"][repo]["team"]
        filter_git_commit_data(repository_name, repository_team)
        create_git_md_table(repository_name)


def clear_file(file_name):
    """
    This function takes a file that clears the content and output's a base table header for a markdown file.
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, 'w')
    heading = "###  Last commits from every repository"
    base_table = '|      Repository      |                   Last commit               |    Deploy time       | \n' + \
                 '|:--------------------:|:-------------------------------------------:|:--------------------:| \n'
    file.write(heading + "\n" + base_table)
    file.close()


def write_main_mk_table(file_name, repository, last_commit, deploy_time):
    """
    This function opens a file (that file should be already created and should contain a markdown table header) and
    appends to it a row that will contain the repository, the last commit and the deploy time.
    :param file_name: Name of the file in which the content is appended. (should also contain the path)
    :param repository: Repository name for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element of the table
    :param deploy_time: Time and Time designator used as the 3rd element of the table
    :return:
    """
    row = "|" + repository + \
          "|" + last_commit + \
          "|" + deploy_time + \
          "|" + '\n'
    write_file = open(file_name, "a")
    write_file.write(row)


def extract_hg_json(json_files):
    """
    Extracts the json data from json files and writes the data to the main markdown table file. The function looks
    into json files after the last commit, extracts it and calls the write_main_mk_table function.

    :param json_files: list of files to extract commits from.
    :return: none
    """
    for file in json_files:
        file_path = "hg_files/" + file

        with open(file_path) as json_files:
            data = json.load(json_files)
            # pprint(data)
            github_base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/hg_files/"
            repository_name = "[" + file.rstrip().replace(".json", "") + "]" + "(" + github_base_link + \
                              file.rstrip().replace(" ", "%20").rstrip().replace(".json", ".md") + ")"

            for test in data:
                commit_description = data.get(test)["commit_message"]
                commit_date = data.get(test)["commit_date"]
                # commit_url = data.get(test)["url"]  # TODO add link to mk table
                write_main_mk_table("main_mk_table.md", repository_name, commit_description, commit_date)
                # We are braking this for loop since we got the last commit.
                break


def extract_github_data(json_files):
    """
    Extracts the json data from json files and writes the data to the main markdown table file. The function looks
    into json files after the last commit, extracts it and calls the write_main_mk_table function.

    :param json_files: list of files to extract commits from.
    :return: none
    """
    for file in json_files:
        file_path = "git_files/" + file

        with open(file_path) as json_files:
            data = json.load(json_files)
            github_base_link = "https://github.com/Akhliskun/firefox-infra-changelog/blob/master/git_files/"
            repository_name = "[" + file.rstrip().replace(".json", "") + "]" + "(" + github_base_link + \
                              file.rstrip().replace(" ", "%20").rstrip().replace(".json", ".md") + ")"

            try:
                for test in data:
                    commit_description = data.get(test)["commit_message"]
                    commit_date = data.get(test)["commit_date"]
                    # commit_url = data.get(test)["url"]  # TODO add link to mk table
                    write_main_mk_table("main_mk_table.md", repository_name, commit_description, commit_date)
                    # We are braking this for loop since we got the last commit.
                    break
            except:
                pass


def generate_main_md_table():
    """
    Looks into repositories folders (hg_files & git files), filters the files to load the json's using a passfilter and
    calls after extraction functions.
    """
    # Get current folder path.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    hg_only_files = [f for f in listdir(dir_path + "/hg_files") if isfile(join(dir_path + "/hg_files", f))]
    git_only_files = [f for f in listdir(dir_path + "/git_files") if isfile(join(dir_path + "/git_files", f))]

    # Pass filter only the ".json" objects
    hg_json_files = [jf for jf in hg_only_files if ".json" in jf]
    git_json_files = [jf for jf in git_only_files if ".json" in jf]

    # Extract data from json_files and writes to main markdown table.
    extract_hg_json(hg_json_files)
    extract_github_data(git_json_files)


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open('./repositories.json').read()
    repositories = json.loads(repositories_data)
    create_files_for_git()
    create_files_for_hg()
    clear_file("main_mk_table.md")
    generate_main_md_table()

