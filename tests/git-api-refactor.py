import requests
import json
import re
import datetime

repoList = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
             'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits'
             }
linkParameters = "?per_page=100&page={}"
debugNumber = 0

try:
    for repoKey in repoList:
        commitsInPage = True
        pageNumber = int(1)
        totalCommits = 0
        while commitsInPage:
            repoLink = repoList[repoKey] + linkParameters.format(int(pageNumber))
            print("Accesing page number:  ", pageNumber, repoKey)
            r = requests.get(repoLink)  # get infos from gitAPI page
            page = r.json()  # turn into JSON content
            for commit in page:
                debugNumber += 1
                totalCommits += 1
            print(totalCommits)
            pageNumber += 1
            if totalCommits % 100 != 0:
                commitsInPage = False
                totalCommits = 0
except Exception as err:
    print("Limit reached \n", err)