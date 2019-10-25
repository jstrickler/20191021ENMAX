#!/usr/bin/env python
import csv

with open('DATA/airport_boardings.csv') as boardings_in:
    rdr = csv.reader(boardings_in)
    headers = next(rdr)
    for name, code, rank2001, total2001, rank2010, total2010, rank2011, total, pct_change1, pct_change2 in rdr:
        print(code, rank2010)
print()

with open('DATA/knights.txt') as knights_in:
    rdr = csv.reader(knights_in, delimiter=":")
    for row in rdr:
        print(row)
print()

data = []
with open('DATA/airport_boardings.csv') as boardings_in:
    rdr = csv.DictReader(boardings_in)
    for row in rdr:
        data.append(row)
#        print(row['Code'], row['2010 Rank'])

print(data[0])
print(data[-1])

print()
