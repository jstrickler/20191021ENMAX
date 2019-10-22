

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

# [EXPR for VAR ... in ITERABLE if COND]
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

foods = ['spam', 'spam', 'spam', 'spam', 'back bacon', 'eggs',
         'spam', 'spam', 'spam', 'beans']

good_foods = [f for f in foods if f != 'spam']
print('good_foods:', good_foods, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [float(n) * 10 for n in nums if n > 300]
print("n1:", n1, '\n')

n2 = []
for n in nums:
    if n > 300:
        n2.append(float(n) * 10)
print("n2:", n2, '\n')

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

dobs = [p[-1] for p in people]
print("dobs:", dobs, '\n')

data = [(i, i**2, i**3) for i in range(1, 11)]
print("data:", data, '\n')

young_geeks = [f"{p[0]} {p[1]}" for p in people if p[-1] > '1970']
print("young geeks:", young_geeks, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f1_gen = (f.upper() for f in fruits)
print(f1_gen)
fruits.append('pumpkin')

for fruit in f1_gen:
    print(fruit)