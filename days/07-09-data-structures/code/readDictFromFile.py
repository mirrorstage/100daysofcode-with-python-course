import re
import pprint

dataPull = r'justTheDictData.txt'
dataDict = {}

# get the data
with open(dataPull) as f:
    dataList = []
    for line in f:
        dataList.append(line)

dataList = dataList[0].split(',')

# make it into a list of 50 lists

for i, d in enumerate(dataList):
    dataList[i] = dataList[i].split(': ')

# mutate contents of list into a dictionary

for entry in dataList:
    dataDict[entry[0]] = entry[1]

pprint.pprint(dataDict)