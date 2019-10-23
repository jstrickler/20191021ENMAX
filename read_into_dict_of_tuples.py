#!/usr/bin/env python
from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip() # remove \n
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = {
            "title": title,
            "color": color,
            "quest": quest,
            "comment": comment,
        }
        # print(name, title, color, quest, comment)

pprint(knight_data)
print()
print(knight_data.get('Bedevere')['quest'], '\n')

for knight, data in knight_data.items():
    print(data['title'], knight, data)
print()

