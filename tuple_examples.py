
person = 'William', 'Shatner', 'Star Trek'
# person = ('William', 'Shatner', 'Star Trek')

print(len(person), person[0], person[1])
print(person[:2], '\n')

first_name, last_name, product = person

print(first_name, product, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]
print(people[0])
print(people[0][1])
print(people[0][1][0])

for first_name, last_name, *product, dob in people:
    # first_name, last_name, *product, dob = next value of people
    print(last_name, product)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

places = [
    ('Calgary', 'Alberta'),
    ('Albany', 'New York'),
    ('Toronto', 'Ontario'),
    ('Haifa', 'Israel'),
]

for city, place in places:
    print(city, place.upper())
print()

for data in places:
    print(data[0], data[1].upper())
print()

animal = 'cat'
p, q, r = animal
print(p)


for data in places:
    print(data)
print()
