import os
import re
import json
import time
import requests
from os import listdir
from github import Github
from os.path import isfile, join
from datetime import datetime, timedelta
import sys
from dateutil.parser import parse
import timestring

lastWeek = datetime.now() - timedelta(days=14)
lastMonth = datetime.utcnow() - timedelta(days=31)
current_dir = os.path.dirname(os.path.realpath(__file__))


def limit_checker():
    """
    This function checks if your limit requests is not exceeded.
    Every time when this function is called, it returns 1 in case of your requests limit is not exceeded,
    otherwise it will wait for the reset time to pass.
    :return: returns 1 if your limit requests is not exceeded
    """
    rate_limit = git.rate_limiting[0]
    unix_reset_time = git.rate_limiting_resettime
    reset_time = datetime.fromtimestamp(unix_reset_time)
    if rate_limit >= 5:
        sys.stdout.write("\rRate limit is: " + str(rate_limit))
        sys.stdout.flush()
        return 1
    else:
        try:
            print("You have reached the requests limit!")
            print("The requests limit will reset at:" + str(reset_time))
            while rate_limit < 5000 and reset_time >= datetime.now():
                unix_reset_time = git.rate_limiting_resettime
                reset_time = datetime.fromtimestamp(unix_reset_time)
            print("\nThe requests limit has been reset!")
            return 1
        except:
            print("The requests limit is reset to:" + str(reset_time))


def create_files_for_git(repositories_holder):
    """
    Main GIT function. Takes every Git repo from a .json file which is populated with repositories and writes all
    the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside git_files/
    """
    for repo in repositories_holder["Github"]:
        repository_name = repo
        repository_team = repositories_holder.get("Github").get(repo).get("team")
        repository_type = repositories_holder.get("Github").get(repo).get("configuration").get("type")
        print("\nWorking on repo: {}".format(repository_name))
        folders_to_check = [x for x in repositories_holder.get("Github").get(repo).get("configuration").get("folders-to-check")]
        filter_git_commit_data(repository_name, repository_team, repository_type, folders_to_check)
        try:
            create_md_table(repository_name, "git_files")
            print("MD table generated successfully")
        except:
            pass
        print("Finished working on {}".format(repository_name))


def get_version(repo_name, repo_team):
    """
    :param repo_name: repository name
    :param repo_team: repository team
    :return: a dictionary with information from the last two release version: latestRelease and previousRelease
    """
    repo_path = repo_team + repo_name
    iteration = 0
    empty_dict = {}
    for tags in git.get_repo(repo_path).get_tags():
        version = tags.name
        sha = tags.commit.sha
        date = tags.commit.commit.last_modified
        date_format = parse(date)
        date = date_format.strftime("%Y-%m-%d %H:%M:%S")
        author = tags.commit.author.login
        if iteration == 0:
            latest_release = {"version": version,
                             "sha": sha,
                             "date": date,
                             "author": author
                             }
            empty_dict.update({"latest_release": latest_release})
            break
    return empty_dict


def compare_files(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path + filename of the modified files. The two lists are mutable.
    :param first_list: First lists.
    :param second_list:  Second list
    :return: returns boolean value in case a match is found.
    """
    for element_f in range(len(first_list)):
        for element_s in range(len(second_list)):
            if str(second_list[element_s]) in str(first_list[element_f]):
                return True
    return False


def get_version_from_build_puppet(version_path, repo_name):
    """
    :param: version_path: Path to the requierments.txt where the version number is stored
    :param: repo_name: The repo for which we are checking the version.
    :return: Returns the version number that is stored in build-puppet for each *scriptworker
    """
    file_to_string = requests.get(version_path).text.split()
    for word in file_to_string:
        if repo_name in word:
            version_in_puppet = re.split("\\b==\\b", word)[-1]
            # the next check makes sure to only return the version in case the repo name appears multiple times
            if version_in_puppet != repo_name:
                return version_in_puppet


def get_commit_details(commit):
    author_info = {}
    files_changed = []
    try:
        commit_sha = commit.sha
    except ValueError:
        commit_sha = "null"
    try:
        commiter_name = commit.author.login
    except ValueError:
        commiter_name = "null"
    try:
        commiter_email = commit.committer.email
    except ValueError:
        commiter_email = "null"
    try:
        commit_message = commit.commit.message
        commit_message = re.sub("[*\n\r]", " ", commit_message)
    except ValueError:
        commit_message = "null"
    try:
        commit_html_url = commit.html_url
    except ValueError:
        commit_html_url = "null"
    try:
        for entry in commit.files:
            files_changed.append(entry.filename)
    except ValueError:
        pass
    try:
        commit_date = commit.commit.author.date
    except ValueError:
        commit_date = "null"

    author_info.update({"sha": commit_sha,
                        "url": commit_html_url,
                        "commiter_name": commiter_name,
                        "commiter_email": commiter_email,
                        "commit_message": commit_message,
                        "commit_date": str(commit_date),
                        "files_changed": files_changed
                        })
    return author_info


def json_writer_git(repository_name, new_commits):
    """
    :param repository_name:
    :param new_commits: a dictionary with the new commits
    :return: write the json file with the old and the new commits
    """
    git_json_filename = "{}.json".format(repository_name)
    try:
        with open(current_dir + "/git_files/" + git_json_filename, "r") as commit_json:
            json_content = json.load(commit_json)  # loads the content of existing json into a variable
    except:
        json_content = ""
    if len(json_content) > 1:
        number = len(new_commits) - 1
        for old_commit in json_content:
            if old_commit != "0":
                number += 1
                new_commits.update({int(number): json_content[old_commit]})

    if len(new_commits) > 0:
        json_file = open(current_dir + "/git_files/" + git_json_filename, "w")
        json.dump(new_commits, json_file, indent=2)
        json_file.close()
    return True


def json_writer_hg(repository_name, new_commits):
    """
        :param repository_name:
        :param new_commits: a dictionary with the new commits
        :return: write the json file with the old and the new commits
        """
    hg_json_filename = "{}.json".format(repository_name)
    try:
        with open(current_dir + "/hg_files/" + hg_json_filename, "r") as commit_json:
            json_content = json.load(commit_json)  # loads the content of existing json into a variable
    except:
        json_content = ""
    # if len(json_content) > 0:
    number = len(json_content) - 1
    for new_commit in new_commits:
        if new_commit == "0":
            json_content["0"] = new_commits[new_commit]
        else:
            if len(new_commits[new_commit].get("changeset_commits")) != 0:
                number += 1
                json_content.update({int(number): new_commits[new_commit]})

    if len(new_commits) > 0:
        json_file = open(current_dir + "/hg_files/" + hg_json_filename, "w")
        json.dump(json_content, json_file, indent=2)
        json_file.close()
    return True


def last_check(repository_name):
    """

    :param repository_name:
    :return: the last time when the repository was checked
    """
    git_json_filename = "{}.json".format(repository_name)
    try:
        with open(current_dir + "/git_files/" + git_json_filename, "r") as commit_json:
            json_content = json.load(commit_json)  # loads the content of existing json into a variable
            try:
                last_checked = datetime.strptime(json_content.get("0").get("lastChecked"), "%Y-%m-%d %H:%M:%S")
                print("Repo last updated on:", last_checked)
            except ValueError:
                last_checked = datetime.strptime(json_content.get("0").get("lastChecked"), "%Y-%m-%d %H:%M:%S.%f")
                print("Repo last updated on:", last_checked)
    except:
        last_checked = lastMonth
    return last_checked


def get_version_from_json(repo_name):
    """
    :param repo_name: name of the repo we are working on
    :return: version our repo was bumped to by the last local commit that we have
    """
    git_json_filename = "{}.json".format(repo_name)
    with open(current_dir + "/git_files/" + git_json_filename, "r") as commit_json:
        json_content = json.load(commit_json)  # loads the content of existing json into a variable
    last_stored_version = json_content.get("0").get("last_releases").get("latest_release").get("version")
    return last_stored_version


def get_date_from_json(repo_name):
    """
    :param repo_name: name of the repo we are currently working on
    :return: date of the last commit that we have locally in our json
    """
    git_json_filename = "{}.json".format(repo_name)
    with open(current_dir + "/git_files/" + git_json_filename, "r") as commit_json:
        json_content = json.load(commit_json)  # loads the content of existing json into a variable
    last_stored_date = json_content.get("0").get("last_releases").get("latest_release").get("date")
    date_format = parse(last_stored_date)
    last_stored_date = datetime.strptime(str(date_format), "%Y-%m-%d %H:%M:%S")
    print("last local date was: ", last_stored_date)
    return last_stored_date


def get_last_local_push_id(repo_name):
    hg_json_filename = "{}.json".format(repo_name)
    with open(current_dir + "/hg_files/" + hg_json_filename, "r") as commit_json:
        json_content = json.load(commit_json)  # loads the content of existing json into a variable
    last_stored_push_id = json_content.get("0").get("last_push_id")
    print("Last local push id is : ", last_stored_push_id)
    return last_stored_push_id


def generate_hg_pushes_link(repo_name):
    start_id = get_last_local_push_id(repo_name)
    if repo_name == "mozilla-central":
        data = json.loads(
            requests.get("https://hg.mozilla.org/mozilla-central/json-pushes?version=2&full=1&startID=15&endID=16").text)
        end_id = data.get("lastpushid")
        generate_pushes_link = "https://hg.mozilla.org/mozilla-central/json-pushes?version=2&full=1&startID={}&endID={}".format(
            start_id, end_id)
    else:
        data = json.loads(
            requests.get(
                "https://hg.mozilla.org/build/{}/json-pushes?version=2&full=1&startID=15&endID=16".format(repo_name)).text)
        end_id = data.get("lastpushid")
        generate_pushes_link = "https://hg.mozilla.org/build/{}/json-pushes?version=2&full=1&startID={}&endID={}".format(repo_name,
            start_id, end_id)
    return generate_pushes_link


def filter_git_commit_data(repository_name, repository_team, repository_type, folders_to_check):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function from 're' library
    :param repository_team:
    :param repository_name: name of the given repo
    :param repository_type: returns the type of a repo we are going to work with
    :param folders_to_check: list that contains every folder we care about from given repo
    :return: Filtered json data
    TODO: please add the exception blocks since the script fails when it can't pull a data:
    (e.g raise self.__createException(status, responseHeaders, output)
            github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    repository_path = repository_team + repository_name
    last_checked = last_check(repository_name)
    new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow())}}
    number = 0
    new_commits = git.get_repo(repository_path).get_commits(since=last_checked)
    # TYPE = NO-TAG
    if repository_type == "no-tag":
        for commit in git.get_repo(repository_path).get_commits(since=last_checked):
            each_commit = {}
            if len(folders_to_check) > 0:  # if greater than 0 compare a list of what files changed
                files_changed = []
                for entry in commit.files:
                    files_changed.append(entry.filename)
                if compare_files(files_changed, folders_to_check):  # checks if any object from list 1 is in list 2
                    number += 1
                    each_commit.update({int(number): get_commit_details(commit)})
                    new_commit_dict.update(each_commit)
            # else we just take all commits
            else:
                number += 1
                each_commit.update({int(number): get_commit_details(commit)})
                new_commit_dict.update(each_commit)

        json_writer_git(repository_name, new_commit_dict)
        return True
    # TYPE = COMMIT-KEYWORD
    if repository_type == "commit-keyword":
        for commit in new_commits:
            files_changed_by_commit = [x.filename for x in commit.files]
            if len(files_changed_by_commit) > 0:
                each_commit = {}
                print(commit.commit.message)
                if "deploy" in commit.commit.message:
                    number += 1
                    each_commit.update({int(number): get_commit_details(commit)})
                    new_commit_dict.update(each_commit)
            json_writer_git(repository_name, new_commit_dict)
        return True
    # TYPE = TAG
    if repository_type == "tag" and repository_name == "build-puppet":
            commit_number_tracker = 1
            pathway = repositories.get("Github").get(repository_name).get("configuration").get("files-to-check")
            for commit in new_commits:
                each_commit = {}
                switch = False
                print("this is commit number: ", commit_number_tracker)
                commit_number_tracker += 1
                files_changed_by_commit = [x.filename for x in commit.files]
                print(files_changed_by_commit)
                print(len(files_changed_by_commit))
                changed_file_number = 1
                for entry in files_changed_by_commit:
                    print("changed file number:  ", changed_file_number)
                    changed_file_number += 1
                    print(entry)
                    for scriptworkers in pathway:
                        print("checking repo: ", scriptworkers)
                        number2 = 0
                        if entry in pathway[scriptworkers]:
                            print(scriptworkers, " needs to be checked.")
                            scriptworker_repo = scriptworkers
                            version_path = repositories.get("Github").get("build-puppet").get("configuration").get("files-to-check").get(scriptworker_repo)
                            latest_releases = get_version(scriptworker_repo, repository_team)
                            version_in_puppet = get_version_from_build_puppet(version_path, scriptworker_repo)
                            print("version is puppet is: ", version_in_puppet)
                            if version_in_puppet == latest_releases.get("latest_release").get("version"):
                                last_local_version = get_version_from_json(scriptworker_repo)
                                print(last_local_version)
                                # if build-puppet and scriptworker repo changelog have the same version after an update
                                if version_in_puppet != last_local_version:
                                    switch = True
                                    last_local_date = get_date_from_json(scriptworker_repo)
                                    new_version_commit_date = datetime.strptime(latest_releases.get("latest_release").get("date"), "%Y-%m-%d %H:%M:%S")
                                    new_scriptworker_dict = {(int(number2)): {"lastChecked": str(datetime.utcnow()),
                                                                              "last_releases": latest_releases}}
                                    new_repo_path = repository_team + scriptworker_repo
                                    for commit2 in git.get_repo(new_repo_path).get_commits(since=last_local_date):
                                        print("modified date: ", commit2.last_modified)
                                        last_modified = datetime.strftime(parse(commit2.last_modified), "%Y-%m-%d %H:%M:%S")
                                        print(last_modified)
                                        last_modified = datetime.strptime(last_modified, "%Y-%m-%d %H:%M:%S")
                                        print(last_modified)
                                        if last_modified <= new_version_commit_date:
                                            each_commit2 = {}
                                            number2 += 1
                                            each_commit2.update({int(number2): get_commit_details(commit2)})
                                            new_scriptworker_dict.update(each_commit2)
                                    json_writer_git(scriptworker_repo, new_scriptworker_dict)
                                    create_md_table(scriptworker_repo, "git_files")
                                else:
                                    print("No new changes entered production")
                            else:
                                switch = True
                                last_commit_date = get_date_from_json(scriptworker_repo)
                                new_version_commit_date = datetime.strptime(latest_releases.get("latest_release").get("date"), "%Y-%m-%d %H:%M:%S")
                                new_scriptworker_dict = {(int(number2)): {"lastChecked": str(datetime.utcnow()),
                                                                          "last_releases": latest_releases}}
                                new_repo_path = repository_team + scriptworker_repo
                                for commit2 in git.get_repo(new_repo_path).get_commits(since=last_commit_date):
                                    print("modified date: ", commit2.last_modified)
                                    last_modified = datetime.strftime(parse(commit2.last_modified), "%Y-%m-%d %H:%M:%S")
                                    print(last_modified)
                                    last_modified = datetime.strptime(last_modified, "%Y-%m-%d %H:%M:%S")
                                    print(last_modified)
                                    if last_modified <= new_version_commit_date:
                                        each_commit2 = {}
                                        number2 += 1
                                        each_commit2.update({int(number2): get_commit_details(commit2)})
                                        new_scriptworker_dict.update(each_commit2)
                                json_writer_git(scriptworker_repo, new_scriptworker_dict)
                                create_md_table(scriptworker_repo, "git_files")
                if switch:
                    number += 1
                    each_commit.update({int(number): get_commit_details(commit)})
                    new_commit_dict.update(each_commit)
            json_writer_git(repository_name, new_commit_dict)
    elif repository_type == "tag" and repository_name != "build-puppet":
        version_path = repositories.get("Github").get(repository_name).get("configuration").get("version-path")
        latest_releases = get_version(repository_name, repository_team)
        if get_version_from_build_puppet(version_path, repository_name) == latest_releases.get("latest_release").get("version"):
            print("No new changes entered production")
        else:
            last_commit_date = get_date_from_json(repository_name)
            new_version_commit_date = datetime.strptime(latest_releases.get("latest_release").get("date"), "%Y-%m-%d %H:%M:%S")
            new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow()),
                                     "last_releases": latest_releases}}
            for commit in git.get_repo(repository_path).get_commits(since=last_commit_date):
                last_modified = datetime.strftime(parse(commit.last_modified), "%Y-%m-%d %H:%M:%S")
                last_modified = datetime.strptime(last_modified, "%Y-%m-%d %H:%M:%S")
                if last_modified <= new_version_commit_date:
                    each_commit = {}
                    number += 1
                    each_commit.update({int(number): get_commit_details(commit)})
                    new_commit_dict.update(each_commit)
            json_writer_git(repository_name, new_commit_dict)
            return True


def create_files_for_hg(repositories_holder):
    """
    Main HG function. Takes every Mercurial repo from a .json file which is populated with repositories and writes all
     the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of repositories
    :return: The end result is a .json and a .md file for every git repository. can be found inside hg_files/
    """
    for repo in repositories_holder["Mercurial"]:
        repository_name = repo
        repository_url = repositories_holder.get("Mercurial").get(repo).get("url")
        folders_to_check = [x for x in repositories_holder.get("Mercurial").get(repo).get("configuration").get("folders-to-check")]
        filter_hg_commit_data(repository_name, folders_to_check, repository_url)
        create_hg_md_table(repository_name)


def filter_hg_commit_data(repository_name, folders_to_check, repository_url):
    """
    This function generates data for hg json files
    :param repository_name: name of the repository
    :return: Writes data in hg json files
    """
    link = generate_hg_pushes_link(repository_name)
    data = json.loads(requests.get(link).text)
    last_push_id = data.get("lastpushid")
    hg_repo_data = {}
    number = 0
    print("\nWorking on repo:", repository_name)
    hg_repo_data.update({"0": {"last_push_id": last_push_id}})
    for key in data.get("pushes"):
        number += 1
        changeset_number = key
        changeset_pusher = data.get("pushes").get(key).get("user")
        date_of_push = data.get("pushes").get(key).get("date")
        hg_repo_data.update({number: {
            "changeset_number": changeset_number,
            "pusher": changeset_pusher,
            "date_of_push": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_of_push)),
            "changeset_commits": {}
        }})
        counter, counter2, counter3 = 0, 0, 0
        for keys in data.get("pushes").get(key).get("changesets"):
            counter = [x + 1 for x in range(len(data.get("pushes").get(key).get("changesets")))]
            node = keys.get("node")
            url = repository_url + "pushloghtml?changeset=" + node[:12]
            author = keys.get("author")
            desc = keys.get("desc")
            files_changed = []
            for entry in keys.get("files"):
                files_changed.append(entry)
            try:
                counter2 = counter[counter3]
                counter3 += 1
            except IndexError:
                pass
            if len(folders_to_check) > 0:
                if compare_files(files_changed, folders_to_check):
                    hg_repo_data[number]["changeset_commits"].update({
                        counter2: {
                              "url": url,
                              "commiter_name": author,
                              "commit_message": desc,
                              "files_changed": files_changed}})
            else:
                hg_repo_data[number]["changeset_commits"].update({
                    counter2: {
                        "url": url,
                        "commiter_name": author,
                        "commit_message": desc,
                        "files_changed": files_changed}})
    json_writer_hg(repository_name, hg_repo_data)


def extract_email(commit_email):
    """
    Helper function!
    Takes as parameter a string that contains between "<" and ">" an email that needs to be extracted.
    The function uses find to search for the beginning of the email (that starts with "<") and adds the lengths of the
    "<" so that returned email doesn't contain the "<" symbol and rfind to find the ending character ">". Both find and
    rfind return the index where the carachters "<" and ">" are placed so when you do return commit_email with
    [start_char_index:ending_char_index] the string shrinks to what's between the characters.
    :param commit_email: String that contains an email
    :return: String that contains only the email
    """
    return commit_email[commit_email.find("<") + len("<"):commit_email.rfind(">")]


def create_md_table(repository_name, path_to_files):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of the MD table
    :param path_to_files: Used to store path to json files (git_files, hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/{}/".format(path_to_files) + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
                     "|:---:|:----:|:----------------------------------:|:------:|:----:| \n"
        tables = {}
        try:
            version = data.get('0').get("last_two_releases").get("LatestRelease").get("version")
            date = data.get('0').get("last_two_releases").get("LatestRelease").get("date")
            md_title = [
                "Repository name: {}\n Current version: {} released on {}".format(repository_name, version, date)]

        except:
            md_title = ["{} commit markdown table since {}".format(repository_name, lastWeek)]
        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            try:
                commit_author = data.get(key).get("commiter_name")
                commit_author = re.sub("\u0131", "i", commit_author)  # this is temporary
                date = data.get(key).get("commit_date")
                message = data.get(key).get("commit_message")
                message = re.sub("\|", "\|", message)
                url = data.get(key).get("url")

                row = "|" + commit_number + \
                      "|" + commit_author + \
                      "|" + message + \
                      "|" + "[URL](" + url + ")" + \
                      "|" + date + "\n"

                del commit_number_list[-1]
                for repo in tables.keys():
                    tables[repo] = tables[repo] + row
            except TypeError:
                pass

        md_file_name = "{}.md".format(repository_name)
        md_file = open(current_dir + "/{}/".format(path_to_files) + md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!".format(repository_name))


def create_hg_md_table(repository_name):
    """
    Uses 'repository_name' parameter to generate markdown tables for every json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of the MD table
    :param path_to_files: Used to store path to json files (git_files, hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(current_dir + "/hg_files/" + "{}.json".format(repository_name)).read()
        data = json.loads(json_data)
        base_table = "| Changeset | Date | Commiter | Commit Message | Commit URL | \n" + \
                     "|:---:|:---:|:----:|:----------------------------------:|:-----:| \n"
        tables = {}
        try:
            last_push_id = data.get('0').get("last_push_id")
            md_title = [
                "Repository name: {}\n Current push id: {}".format(repository_name, last_push_id)]

        except:
            md_title = ["{} commit markdown table since push id: {}".format(repository_name, last_push_id)]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            if key > "0":
                key = str(len(data) - int(key))
                changeset_id = data.get(key).get("changeset_number")
                date_of_push = data.get(key).get("date_of_push")
                try:
                    for entry in data.get(key).get("changeset_commits"):
                        try:
                            commit_author = data.get(key).get("changeset_commits").get(entry).get("commiter_name")
                            commit_author = re.sub("\u0131", "i", commit_author)  # this is temporary
                            message = data.get(key).get("changeset_commits").get(entry).get("commit_message")
                            message = re.sub("\n|", "", message)
                            url = data.get(key).get("changeset_commits").get(entry).get("url")

                            row = "|" + changeset_id + \
                                  "|" + date_of_push + \
                                  "|" + commit_author + \
                                  "|" + message + \
                                  "|" + url + "\n"

                            for repo in tables.keys():
                                tables[repo] = tables[repo] + row
                        except TypeError:
                            pass
                except TypeError:
                    pass

        md_file_name = "{}.md".format(repository_name)
        md_file = open(current_dir + "/hg_files/" + md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        print("Json for {} is empty! Skipping!".format(repository_name))


def clear_file(file_name):
    """
    This function takes a file that clears the content and output's a base table header for a markdown file.
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, "w")
    heading = "##  Commits in production. \n"
    file.write(heading)
    file.close()


def generate_main_md_table(path_to_files):
    """
    Looks into repositories folders (hg_files & git files), filters the files to load the json's using a passfilter and
    calls after extraction functions.
    :param path_to_files: Folder to json files
    """
    # Get current folder path.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/{}".format(path_to_files)) if
                  isfile(join(dir_path + "/{}".format(path_to_files), f))]

    print("only files: ", only_files)

    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]

    # Extract data from json_files and writes to main markdown table.
    extract_json(json_files, path_to_files)

    print("Table successfully generated.")


def extract_reviewer(string):
    """
    Helper function!
    Takes the string on the input and looks for a specific set of characters (either "r=" or "a=").
    If at least one of them are present (most of the times they are in the mercurial world) then this function will
    return the reviewer/approved by names.
    If none of them are present, the function will return an empty string.
    :param string: usually the commit message.
    :return: a string that may contain the author name (if "r=" or "a=" exists)
    """
    reviewer = ""
    approved_by = ""
    try:
        reviewer = string.split("r=")[1].split()[0]
    except IndexError:
        pass
    try:
        approved_by = string.split("a=")[1].split()[0]
    except IndexError:
        pass

    if len(reviewer) < 1:
        return approved_by
    else:
        return reviewer


def extract_json(json_files, path_to_files):
    """
    Extracts the json data from json files and writes the data to the main markdown table file. The function looks
    into json files after the last commit, extracts it and calls the write_main_md_table function.
    :param commits_per_repo: number of commits to be used in the main markdown file
    :param json_files: List of files to extract commits from.
    :param path_to_files: Folder to json files
    :return: none
    """
    time_24h_ago = datetime.utcnow() - timedelta(days=1)
    test = datetime.strftime(time_24h_ago, "%Y-%m-%d %H:%M:%S")
    time_24h_ago = datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

    for file in json_files:
        file_path = "{}/".format(path_to_files) + file
        with open(file_path) as json_files:
            data = json.load(json_files)
            base_link = "https://github.com/mozilla-releng/firefox-infra-changelog/blob/master/{}/".format(path_to_files)
            repository_url = base_link + file.rstrip().replace(" ", "%20").rstrip().replace(".json", ".md")
            repository_json = base_link + file.rstrip().replace(" ", "%20")
            repository_title = file.replace(".json", "")
            try:
                # Generates the markdown header for a specific repository
                generate_markdown_header("main_md_table.md", repository_title, repository_url, repository_json)
                # Write the commits from json files into the main markdown table
                if path_to_files == "git_files":
                    if "0" in data:
                        del data["0"]
                        print("0 deleted")
                    for commit_iterator in data:
                        commit_number = str(commit_iterator)
                        commit_date = data.get(commit_number).get("commit_date")
                        is_it_under_24 = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")
                        print(is_it_under_24, "vs ", time_24h_ago)
                        if is_it_under_24 > time_24h_ago:
                            commit_description = data.get(commit_number).get("commit_message")
                            commit_url = data.get(commit_number).get("url")
                            commit_url = "[Link](" + commit_url + ")"
                            author = data.get(commit_number).get("commiter_name")
                            review = "Placeholder"  # TODO git handler for getting the reviewer.

                            write_main_md_table("main_md_table.md",
                                                commit_url,
                                                commit_description,
                                                author,
                                                review,
                                                commit_date)
                elif path_to_files is "hg_files":
                    if "0" in data:
                        del data["0"]
                    else:
                        for changeset_iterator in data:
                            for commit_iterator in data.get(changeset_iterator).get("changeset_commits"):
                                commit_number = str(commit_iterator)
                                commit_date = data.get(changeset_iterator).get("date_of_push")
                                is_it_under_24 = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")
                                if is_it_under_24 > time_24h_ago:
                                    commit_description = commit_iterator.get("commit_message")
                                    commit_url = commit_iterator.get("url")
                                    commit_url = "[Link](" + commit_url + ")"
                                    author = data.get(changeset_iterator).get("pusher")
                                    review = extract_reviewer(commit_description)
                                    write_main_md_table("main_md_table.md",
                                                        commit_url,
                                                        commit_description,
                                                        author,
                                                        review,
                                                        commit_date)
            except KeyError:
                print("File " + file + " is empty. \nPlease check:" + repository_url + " for more details.\n")
                pass
            except AttributeError:
                pass


def generate_markdown_header(file_name, repository_name, markdown_link, json_link):
    """
    This function appends the markdown header to the main markdown table. It includes the repository title (name), the
    markdown link and the json link.
    :param file_name: name of the file in which the content it's added.
    :param repository_name: name of the repository for the generated table.
    :param markdown_link: markdown link for the header table.
    :param json_link: json link for the header table.
    :return: none, expected to write to file_name.
    """
    file = open(file_name, "a")

    repository_title = "|\t" + repository_name + "\t|\t" + "[MarkDown](" + markdown_link + ")" + "\t|\t" + "[Json](" + \
                       json_link + ")" + "\t| \n"

    title_table_formation = "|:----------:|:-----------------------:|:--------:| \n "

    base_table = "| Link | Last commit | Author | Reviewer | Deploy time | \n" + \
                 "|:----------:|:-----------:|:------:|:--------:|:-----------:| \n"

    file.write("\n" + repository_title + title_table_formation + "\n" + base_table)
    file.close()


def write_main_md_table(file_name, repository_url, last_commit, author, reviewer, deploy_time):
    """
    This function opens a file (that file should be already created and appends to it a row that will contain the
    repository, the last commit and the deploy time.
    :param file_name: Name of the file in which the content is appended. (should also contain the path)
    :param repository_url: Repository url for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element of the table
    :param deploy_time: Time and Time designator used as the 3rd element of the table
    :return:
    """
    row = "|" + repository_url + \
          "|" + last_commit + \
          "|" + author + \
          "|" + reviewer + \
          "|" + deploy_time + \
          "|" + "\n"
    write_file = open(file_name, "a")
    write_file.write(row)


if __name__ == "__main__":
    TOKEN = os.environ.get("GIT_TOKEN")
    git = Github(TOKEN)
    repositories_data = open("./repositories.json").read()
    repositories = json.loads(repositories_data)
    # create_files_for_git(repositories)
    # create_files_for_hg(repositories)
    # clear_file("main_md_table.md")
    generate_main_md_table("hg_files")
    generate_main_md_table("git_files")
