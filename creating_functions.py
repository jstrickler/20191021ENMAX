#!/usr/bin/env python


# DEFINE function
def print_message():
    message = get_message()
    print(message.upper())

def get_message():
    return "Hello, ENMAX world"

m = get_message()

print(m)

# CALL function
print_message()

def greet(whom):  # whom is parameter
    print("Hello,", whom)

greet("Mom")  # "Mom" is argument
greet("Andrew Sheer")
greet("Justin Trudeau")

person = "Bill Gates"
greet(person)

def make_line(line_character='-', size=50):
    return line_character * size

print(make_line('-', 10))
print(make_line('=', 40))
print(make_line('*'))
print(make_line())

def say_hello(greeting, *people):
    for person in people:
        print(greeting, person)
    print()

say_hello("Hi", "Mom")
say_hello("Howdy", "Mom", "Dad", "Uncle Herbert")
say_hello("Greetings")



