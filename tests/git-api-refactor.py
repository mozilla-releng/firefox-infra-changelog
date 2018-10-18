import requests
import json
import re
import datetime

repoList = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
             'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits'
             }
linkParameters = "?per_page=5&page={}"
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
            pageNumber += 200

            if r.text == "b[]":
                print("Nothing in page.")
                commitsInPage = False

        print(totalCommits)


except Exception as err:
    print("Limit reached \n", err)