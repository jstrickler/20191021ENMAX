
colors = ['red', 'white', 'green', 'yellow', 'blue']
print(len(colors), min(colors), max(colors))

print(sorted(colors))

rev_colors = reversed(colors)
print(rev_colors)

for color in rev_colors:
    print(color)
print()

cities = ['Calgary', 'Vancouver', 'Ottawa']
provences = ['AB', 'BC', 'ON']

places = zip(cities, provences)
print(places)
print(list(places))

places = zip(cities, provences)
for place in places:
    print(place)
print()