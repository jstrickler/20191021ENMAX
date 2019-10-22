
things = ['maple syrup', 'hockey', 'Timbits']

for i, t in enumerate(things):
    print(i, t)
print()

print(list(enumerate(things)))

actor = "hweolrllod"

for i, char in enumerate(actor[::2], 1):
    print(i, char)

for i, char in enumerate(actor[1::2], 1):
    print(i, char)
