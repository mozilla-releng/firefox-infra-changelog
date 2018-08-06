import requests
import json
import pprint

json_data=open('./github_changelog.json').read()

data = json.loads(json_data)

#e.g1:
#print(data['shipit']['0']['Name: '])  #print name from commit 0 from repo shipit

#e.g2:
#for key in data:
 #   print(data[key]['0']['Name: '])   #print the name from commit 0 from each repo

#e.g3:
for key in data:                       #print each name from each commit from each repo
    print('\n' + 'Repository: ' + key + '\n')
    for keys in data[key]: 
        print('Commit number: ' + keys)
        print('Name: ' + data[key][keys]['Name: '])