#!/usr/bin/env python

i1 = 100
s = "100"
print(i1 * 3, s * 3)
i2 = 0b100
print(i2 * 10)
i3 = 0x100
print(i3 * 10)
i4 = 0o100
print(i4 * 10)

f0 = 1.23
f1 = .23
f2 = 1.
f3 = 1.23e15
f4 = 12.0

c1 = 50j
print(c1, type(c1))

a = 19
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
print(divmod(a, b))

x = 5
x += 5   # x = x + 5
x *= 3   # x = x * 3
x /= 6   # x = x / 6
print(x)

print("moose" * 10)

# x = 5
# y = x++
# z = ++x
# print(x, y, z)

# ( parentheses )
# [ brackets }
# { braces }
print(5 + 8 / 9 * 3)
print((5 + 8) / (9 * 3))
print(5 + (8 / 9) * 3)
print((5 + 8) / 9 * 3)

# PEMDAS

a = "1234"
aa = int(a)
print(a, aa)
print(a * 3, aa * 3)

b = "DeadBeef"
bb = int(b, 16)
print(b, bb)

print(str(5))

print(bool(5), bool(0), bool("wut?"))

