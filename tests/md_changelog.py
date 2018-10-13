import requests
import json
import markdown
import re

'''This file gather all the information from the hg and git json files and store them into the changelog.md file as a table '''

git_logs=open('../tests/github_changelog.json').read()  #opend json file with read permission
git_data = json.loads(git_logs) #add all the infos into git_data
hg_logs=open('../tests/hg_changelog.json').read() 
hg_data = json.loads(hg_logs)

f = open('../tests/changelog.md', "a")    #open the .md file 
changelogs_hg = {}   #hg dictionary
changelogs_git = {}  #git dictionary
changelogs = {}  #main dictionary
title = "### GIT" + "\n"  #header fro GIT table
header = "| Repository | Commiter | Email | Time | URL | Message |" + "\n" + "| --- | --- | --- | --- | --- | --- |" + "\n"  # table header

f.write(title)  #write the headers into the file
f.write(header)
for key in git_data:              #for loop to scroll through the git data          
    repository = key   #current repository
    for keys in git_data[key]:  #for loop to scroll through the git commits
        commiter_name = git_data[key][keys]['Name: ']
        commiter_email = git_data[key][keys]['Email: '] 
        commit_date = git_data[key][keys]['Date: '] 
        commit_url = git_data[key][keys]['Url: '] 
        commit_message = git_data[key][keys]['Message: ']
        row_line = ('|' + repository + '|' + commiter_name + '|' + commiter_email + '|' + commit_date + '|' + commit_url + '|' + commit_message + '|' + '\n')   #add each info into the row line
        f.write(row_line)  #write the row line into the table
title = "### Mercurial" + "\n"
header = "| Repository | Commiter | Time | Node | Message |" + "\n" + "| --- | --- | --- | --- | --- |" + "\n"   #the header for the hg table

f.write(title)
f.write(header)    #write the header into the .md file
for key1 in hg_data:    #for loop to scroll through the hg hg data 
    repository = key1   #the current repository
    for keys1 in hg_data[key1]:  #for loop to scroll through the hg commits
        commiter_name = hg_data[key1][keys1]['Name: ']
        commit_date = hg_data[key1][keys1]['Date: ']
        commit_message = hg_data[key1][keys1]['Message: ']
        commt_node = hg_data[key1][keys1]['Node: ']
        row_line = ('|' + repository + '|' + commiter_name + '|' + commit_date + '|' + commt_node + '|' + commit_message + '|' '\n')    #row line with each commit infos
        f.write(row_line)  #write the row line into the table