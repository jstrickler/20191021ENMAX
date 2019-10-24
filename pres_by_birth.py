#!/usr/bin/env python

president_list = []

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        president_list.append(fields)

# print(president_list)

def by_birth(p):
    return p[3]

for _, last_name, first_name, birthdate,  *_, party in sorted(president_list, key=by_birth):
    print(first_name, last_name, birthdate, party)

