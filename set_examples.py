#!/usr/bin/env python

ann_countries = [
    "Canada", 'New Zealand', 'UK',
    "India", "US", "South Africa",
    "US", "US", "US", "US", "US", "US",
]

mary_countries = [
    "Israel", "Bulgaria", "Canada", "UK",
    "China", "Latvia", "Lithuania"
]

ann = set(ann_countries)
mary = set(mary_countries)
for i in range(1000000):
    mary.add("India")

print("ann:", ann)
print("mary:", mary)
print()

print("common:", ann & mary)  # intersection
print("not common:", ann ^ mary) # Xor
print("all:", ann | mary) #  union
print("Ann only:", ann - mary)
print("Mary only:", mary - ann)


if "Bulgaria" in mary:
    print("Mary has been to Bulgaria")

