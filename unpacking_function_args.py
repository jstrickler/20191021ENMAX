#!/usr/bin/env python

def spam(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("----")

spam(1, 2, 3)
spam('a', 'b', 'c')

values = [5, 10, 15, 20, 25]

# NO!!
# spam(values[0], values[1], values[2])

spam(*values[:3])
spam(*values[-3:])



