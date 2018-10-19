import requests
import json
import pprint

'''This file gather all the information from each json file (Hg and GIt) and store them into the main json file (changelog.json) '''

git_logs=open('../tests/github_changelog.json').read()  #open .json file to read the dates
git_data = json.loads(git_logs)  #add the infos into git_date 
hg_logs=open('../tests/hg_changelog.json').read() #--||--HG
hg_data = json.loads(hg_logs) #--||--HG

changelogs_hg = {}  #GIT: dictionary with key = repository name and value = all the commit infos
changelogs_git = {} #HG: --||--
changelogs = {}  #the maine dictionary

for key in git_data:                  #for loop to scroll through git data json     
    git_repo = {}  #dictionary with key=commit number and value = commit infos
    for keys in git_data[key]:  #for loop to scroll through commits
        git_repo.update( { keys : [git_data[key][keys]['Name: '],    #add all infos from each commit into git_repo dictionary
                                   git_data[key][keys]['Email: '],
                                   git_data[key][keys]['Date: '],
                                   git_data[key][keys]['Url: '],
                                   git_data[key][keys]['Message: ']] } )
    changelogs_git.update({ key : git_repo })    #add each commit infos from each repo into dictionary

for key1 in hg_data:    #for loop to scroll through HG data json
    hg_repo = {}   #dictionary with key=commit number and value= commit infos
    for keys1 in hg_data[key1]:  #for loop to scroll through each commit
        hg_repo.update( { keys1 : [hg_data[key1][keys1]['Name: '],   #save the commit dates into hg_repo dictionary
                                   hg_data[key1][keys1]['Date: '],
                                   hg_data[key1][keys1]['Message: '],
                                   hg_data[key1][keys1]['Node: ']]} )
    changelogs_hg.update( { key1: hg_repo} )  #save each commit from each repo into changelog_hg dictionary

changelogs = { 'Git: ' : changelogs_git,   #add all the commit dates from GIT and HG into changelogs dictionary
               'Mercurial: ' : changelogs_hg }

with open('../tests/changelog.json', 'w') as fp:   #open the main json file and add into it the changelogs dictionary
    json.dump(changelogs, fp)