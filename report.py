#!/usr/bin/python
import sys
import datetime
import re
now = datetime.datetime.now()
month = sys.argv[1] if len(sys.argv) >= 2 else str(now.month).zfill(2)
year = str(now.year - 1 if now.month == 1 and month > 1 else now.year)

f = open("time.time", "r")

rightYear = False
rightMonth = False
report = {'h': 0, 'r': 0, 'p': 0, 'v': 0, 'b': 0 }
fieldAbbrs = {
    'h': 'Hours',
    'r': 'Returns',
    'p': 'Placements',
    'v': 'Videos',
    'b': 'Bible Studies'
}

for line in f:
    if len(line) == 3 and rightYear:
        rightMonth = month in line
    if len(line) == 5:
        rightYear = year in line
    if rightMonth and len(line) > 2:
        day = line.split(";")[1:-1]
        for field in day:
           count, unit = re.findall(r'^([\d.]+)([bhprv])$', field)[0]
           report[unit] += float(count)
f.close()

for unit, total in report.items():
    if total > 0:
        print(total, fieldAbbrs[unit])
