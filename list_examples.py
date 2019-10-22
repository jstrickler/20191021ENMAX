import sys

print(sys.argv)
print(sys.argv[0])

colors = ['red', 'green', 'blue']
print(colors[1], len(colors))

name = 'Tim Horton'
print(name[1], name[5], len(name))

#  tuple, bytes, list, str
# sequence types, collections, array types

print(colors.count('red'), name.count('or'))

cities = ['Calgary', 'Banff', 'Kamloops',
    'Edmonton', 'Lake Louise']

print(cities[0], cities[3])

cities.append("Saskatoon")
print(cities, '\n')

cities.insert(0, 'Red Deer')
print(cities, '\n')

more_cities = ['Canmore', 'Medicine Hat',
    "Lethbridge"]
cities.extend(more_cities)
print(cities, '\n')

print(dir(cities), '\n')

s_index = cities.index('Saskatoon')
print(s_index)
del cities[s_index]
print(cities, '\n')
x = cities.pop()
print(x)
print(cities, '\n')
x = cities.pop(2)
print(x)
print(cities, '\n')

cities.remove('Kamloops')
print(cities, '\n')

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[4], fruits[-1], fruits[-2] )
actor = 'William Shatner'
print(actor[0], actor[-1], '\n')

new_fruits = [fruits[0], fruits[1], fruits[2]]
print(new_fruits, '\n')
new_fruits = fruits[0:3]
print(new_fruits, '\n')

#    C[start:stop]   C[start:]  C[:stop] C[start:stop:step]
print(fruits[4:7])
print(fruits[:5])  # first 5
print(fruits[15:])
print(fruits[-5:])
print(actor[:4], actor[-7:], actor[10:12])

f2 = fruits[::]
f3 = list(fruits)
f4 = fruits  # NOT A REAL COPY!!! DANGER DANGER !!!

print(fruits, '\n')

for fruit in fruits:
    print(fruit)
print()

# for VAR... in ITERABLE:
#     VAR = next ITERABLE
#     code....
char = 'z'
for char in actor:
    #  char = next actor
    if char == ' ':
        break
    print(char)
print()
print("char is", char)
print()