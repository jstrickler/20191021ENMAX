#!/usr/bin/env python

president_list = []

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        line = raw_line.rstrip()
        fields = line.split(':')
        president_list.append(fields)

def by_birth(p):
    return p[3]


