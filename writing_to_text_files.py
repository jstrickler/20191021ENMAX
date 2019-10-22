
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in sorted(fruits):
        # fruitlist_out.write(fruit + '\n')
        print(fruit)
        fruitlist_out.write(f"{fruit}\n")

with open('DATA/alice.txt', 'r') as alice_in:
    with open('lizard.txt', 'w') as lizard_out:
        for line in alice_in:
            if 'lizard' in line.lower():
                lizard_out.write(line)
