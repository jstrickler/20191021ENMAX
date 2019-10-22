#!/usr/bin/env python

print("Welcome to ticket sales\n")

while True:  # <1>
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # <2>
    elif raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # <3>
    elif raw_quantity.strip().replace('.', '').isdigit():
        quantity = int(raw_quantity)
        print("sending {} ticket(s)".format(quantity))
    else:
        print("Please enter a number")
