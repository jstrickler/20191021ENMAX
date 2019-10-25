#!/usr/bin/env python
import sys
import csv

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry "Perl Guy"', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux, Git', '1969-12-28'),
]

with open('computer_people.csv', 'w') as cp_out:
    if sys.platform == 'win32':
        wtr = csv.writer(cp_out, lineterminator='\n')
    else:
        wtr = csv.writer(cp_out)
    for person in people:
        wtr.writerow(person)  # pass an ITERABLE
