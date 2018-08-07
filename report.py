#!/usr/bin/python
import sys
import datetime
import re
now = datetime.datetime.now()
year = str(now.year)
month = sys.argv[1] if len(sys.argv) >= 2 else str(now.month).zfill(2)

f = open("time.time", "r")

rightYear = False
rightMonth = False
report = {'h': 0, 'r': 0, 'p': 0, 'v': 0, 'b': 0 }

for line in f:
    if len(line) == 3 and rightYear:
        rightMonth = month in line
    if len(line) == 5:
        rightYear = year in line
    if rightMonth and len(line) > 2:
        day = line.split(";")[1:-1]
        for field in day:
           count, unit = re.findall(r'^(\d+)([bhprv])$', field)[0]
           report[unit] += int(count)
f.close()

print("report for", month, year, report)
