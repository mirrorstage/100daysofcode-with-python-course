from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

# for you to code:

def convert_to_datetime(line):
    regex = re.compile(r'\d\d\d\d-..-..T..:..:..')
    mo = regex.search(line)
    ts = datetime.strptime(mo.group(), '%Y-%m-%dT%H:%M:%S')
    return ts

##def convert_to_datetime_alt(line):
##    timestamp = line.split()[1]
##    date_str = '%Y-%m-%dT%H:%M:%S'
##    return datetime.strptime(timestamp, date_str)
## # source: https://daveyoon64.com/2018/04/23/devops-101-parsing-logs/

def time_between_shutdowns(loglines):
    eventList = []
    shutdownList = []    
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            eventList.append(line)
    for event in eventList:
        eventDatetime = convert_to_datetime(event)
        shutdownList.append(eventDatetime)
    if type(event) in shutdownList == 'str':
            shutdownList.remove(event)
    td = shutdownList[1] - shutdownList[0]
    return td