"""
This module contains functions that are for other scopes which aim to get
better functionality out of the code and not directly related to the script.
"""
import re
import json
from github import GithubException
from fic_modules.configuration import (
    REPOSITORIES,
    REPO_LIST,
    GIT,
    LOGGER
)
from datetime import datetime


def compare_files(first_list, second_list):
    """
    Compares two lists that should contain the path + filename of the modified
    files. The two lists are mutable.
    :param first_list: First lists.
    :param second_list:  Second list
    :return: returns boolean value in case a match is found.
    """
    for element_f in range(len(first_list)):
        for element_s in range(len(second_list)):
            if str(second_list[element_s]) in str(first_list[element_f]):
                return True


def clear_file(file_name, generated_for_days=1):
    """
    This function takes a file that clears the content and output's a base
    table header for a markdown file.
    :param generated_for_days: used for generate the title (default being set
    for one day)
    :param file_name: Name of the file to be written. (should also contain the
    path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, "w")
    if generated_for_days == 1:
        heading = "##  Commits in production - for one day, generated on: " \
                  + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) + \
                  " UTC."
    else:
        heading = "##  Commits in production - for " + \
                  str(generated_for_days) + " days" + ", generated on: " \
                  + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) + \
                  " UTC."
    file.write(heading)
    file.close()


def get_commit_details(commit):
    """
    Extracts sha, url, commiter name, commiter email, commiter message, commit
    date and files_changed from a commit object and stores them in a dictionary
     that gets returned at the end.
    :param commit: commit object that should contain information about commit.
    :return: a dictionary with extracted data, properly formatted.
    """
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


def extract_email(commit_email):
    """
    Takes as parameter a string that contains between "<" and ">" an email
    that needs to be extracted.
    The function uses find to search for the beginning of the email (that
    starts with "<") and adds the lengths of the "<" so that returned email
    doesn't contain the "<" symbol and rfind to find the ending character ">".
    Both find and rfind return the index where the carachters "<" and ">" are
    placed so when you do return commit_email with
    [start_char_index:ending_char_index] the string shrinks to what's
    between the characters.
    :param commit_email: String that contains an email
    :return: String that contains only the email
    """
    return commit_email[commit_email.find("<") +
                        len("<"):commit_email.rfind(">")]


def extract_reviewer(string):
    """
    Takes the string on the input and looks for a specific set of characters
    (either "r=" or "a=").
    If at least one of them are present (most of the times they are in the
    mercurial world) then this function will return the reviewer/approved by
    names.
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


def remove_chars(string, char):
    """
    Removes a specific character from a string
    :param string: string that contains a special char
    :param char: char to be removed from string
    :return: returns a string without char.
    """
    return re.sub(char, " ", string)


def filter_strings(string):
    """
    Filters the provided string and removes specific words/characters from it
    that are stored in unwanted_chars variable.
    This filter removes chars that can't be written to the markdown file
    (since the encoding of those is not supported).
    :param string: string to be filtered
    :return:
    """
    unwanted_chars = ["\u0131", "\u30c4", "\u00c1", "\u00ee", "\u0103",
                      "\u00e4", "\u00e8", "\u2013", "\U0001f60b", "\u00af",
                      "\U0001f92a"]

    for word in string:
        if word in unwanted_chars:
            string = remove_chars(string, word)

    return string


def limit_checker():
    """
    This function checks if your limit requests is not exceeded.
    Every time when this function is called, it returns 1 in case of your
    requests limit is not exceeded, otherwise it will wait for the reset time
    to pass.
    :return: returns 1 if your limit requests is not exceeded
    """
    rate_limit = GIT.rate_limiting[0]
    unix_reset_time = GIT.rate_limiting_resettime
    reset_time = datetime.fromtimestamp(unix_reset_time)
    if rate_limit >= 5:
        LOGGER.info("Rate limit is: %s", str(rate_limit))
        return True
    else:
        try:
            LOGGER.info("You have reached the requests limit!")
            LOGGER.info("The requests limit will reset at: %s", str(reset_time))
            while rate_limit < 5000 and reset_time >= datetime.now():
                unix_reset_time = GIT.rate_limiting_resettime
                reset_time = datetime.fromtimestamp(unix_reset_time)
            LOGGER.info("The requests limit has been reset!")
            return True

        except GithubException.status == 403:
            LOGGER.info("The requests limit is reset to: %s", str(reset_time))
        except GithubException.status == 404:
            LOGGER.info("Github is down!\n Please try again later...")


def get_keys(name):
    """
    :param name: Name of the platform
    :return: A list with all available repositories
    """
    for key in REPOSITORIES.get("{}".format(name)):
        REPO_LIST.append(key)
    return REPO_LIST


def replace_bug_with_url(message, LOGGER):
    """
    This function generates and replaces bug numbers with bugzilla links in commit messages.
    Supports MD format.
    :param message: commit message
    :param LOGGER: send the logger object
    :return: the commit message with formatted bug link for MD files.
    """
    commit_text = message.split()
    for element in range(len(commit_text)):
        if commit_text[element].lower() == "bug" and element < len(commit_text) - 1:
            bug_number = re.sub("[(:,.;)]", "", commit_text[element + 1])
            try:
                bug_number = int(bug_number)
                generated_link = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + \
                                 str(bug_number)
                commit_text[element] = '[' + 'Bug' + ' ' + str(bug_number)
                commit_text[element + 1] = '](' + generated_link + ')'
            except ValueError:
                if LOGGER.root.level == 30:
                    LOGGER.warning("Invalid bug number: > {} < in message: {}"
                                 .format(commit_text[element + 1], message))
    commit_text = ' '.join(commit_text)
    return commit_text


def populate_changelog_json(work_dir, repo_name):
    """
    Takes the data from within json files and prepares it for changelog.json
    :param work_dir:
    :param repo_name:
    :return: returns all the data from a single json file
    """
    json_file = open(work_dir + repo_name + ".json", "r")
    content = json.load(json_file)
    try:
        del content["0"]
    except KeyError:
        pass
    data = {}
    data.update({repo_name: content})
    return data


def write_to_changelog_json(dict_name, platform):
    """
    Update changelog.json with changes from only Git or Hg
    :param dict_name: data that gets written to the json
    :param platform: expects Hg or Github
    :return:
    """
    with open("changelog.json", "r") as file:
        file_content = json.load(file)
    file_content.update({str(platform): dict_name})
    data_file = open("changelog.json", "w")
    json.dump(file_content, data_file, indent=2)
    data_file.close()
