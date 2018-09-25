import os
import urllib.request
import re

# dataLocation = 'https://raw.githubusercontent.com/talkpython/100daysofcode-with-python-course/master/days/07-09-data-structures/code/data.py'
# rawData = os.path.join('/tmp', 'some-data.py')
# urllib.request.urlretrieve(dataLocation, rawData)

parsedData = []
parsedStateAbbrevs = []
parsedDict= {}

# for item in parsedDict.items():

with open('/tmp/some-data') as f:
    for line in f:
        line = line.lstrip()
        try:
            key, value = line.split(':')
            parsedDict[key] = value
        except ValueError:
            continue

abbrevsRegex = re.compile(' |,|\'|\\|n')

for value in parsedDict.values():
    tmp = abbrevsRegex.sub('', value)
    value = tmp



print(parsedDict.values())

        # line = line.splitlines()
        # parsedData = parsedData + line

# for x in range(3, 53, 2):
#     parsedStateAbbrevs.append(parsedData[x].lstrip())

# for x in parsedStateAbbrevs:
#     parsedDict['States'] = parsedStateAbbrevs[x]


# 1) import US States data structures from course repo
#    Requirement: URL
#    Requirement: os module
#    Requirement: requests module or urllib module
#    Action: create objects to serve as containers for the download
#    Action: download from the repo and assign into the objects
#    Action: create objects into which lines of downloads can be assigned

# 2) run the following operations on the data
#    Action: Print out the 10th item in each.
#    Action: Print out the 45th key in the dictionary.
#    Action: Print out the 27th value in the dictionary.



#    Requirement: 
#    Action: 