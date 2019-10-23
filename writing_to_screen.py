#!/usr/bin/env python

actor = "Dan Ackroyd"
place = "Hollywood"

result = 19/3.1

print(actor, place, result)
print("next line")
print("another line")
print("and another")
print(5, 5, 5, 5, 5)

print("next line", end="|")
print("another line", end="/")
print("and another")

print('foo', end='')
print('bar')

print(actor, place, sep="==>")
print(actor, place, sep=" ==> ")

a = 5
b = 10
c = 15
print(a, b, c, sep="::")

#      0           1          0      1
print("{} lives in {}".format(actor, place))
print(f"{actor} lives in {place}")

print(result)
print("{:.2f}".format(result))
print(f"{result:.2f}")

big_number = 3238529358293582395823
print("{:,d}".format(big_number))

medium_number = 1_234_839

weird_number = 12_34_83_9

