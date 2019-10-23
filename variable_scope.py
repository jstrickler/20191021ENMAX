#!/usr/bin/env python

# try not to have global variables

x = 100 # global variable

def spam():
    x = 42  # local variable
    print("x is", x)
    y = "Santa Claus" # local variable

spam()
# print("y is", y)
print("x is", x)

