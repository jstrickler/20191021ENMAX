#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(s):
    print()
    lower_s = s.lower()
    print("orig value:", s)
    print("sort value:", lower_s)
    return lower_s

# spam(1, 2, 3)
# ham(file_name='foo.txt', user_name='rhonda')

def floob():
    return "moose"

m = floob()


f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

def goofy_sort(f):
    return f[1].lower()

f3 = sorted(fruits, key=goofy_sort)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

f5 = sorted(fruits, key=str.lower)
print("f5:", f5, '\n')

def moose(f):
    return len(f), f.lower()

f6 = sorted(fruits, key=moose)
print("f6:", f6, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[3]

for first_name, last_name, product, dob in sorted(people, key=by_dob):
    print(first_name, last_name, dob)
print()

def by_last_name(p):
    return p[1].lower(), p[0].lower()

for first_name, last_name, product, dob in sorted(people, key=by_last_name):
    print(first_name, last_name)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'YYC': 'Calgary',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'YOW': 'Ottawa',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'IAD': 'Dulles',
    'YYZ': 'Toronto',
    'YYR': 'Regina',
    'YEG': 'Edmonton',
    'YVR': 'Vancouver',
}

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(item):
    return item[1], item[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()


