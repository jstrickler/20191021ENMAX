#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

#  \n \r \f \t \b
print(len(s1))
print(len(s2))
print(len(s5))
print("Guido's the man!")
print('Guido was the "BDFL" of Python')

print("""Guido's the ex-"BDFL" of Python""")

query = """
    select *
    from customers
    where postal_code = "1a2 z2f"
"""

print("It is 20\u00B0 in Durham")
