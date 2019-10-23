#!/usr/bin/env python

actor = "Dan Ackroyd"

a1 = actor.upper()
print(a1)
print(actor.upper())
print(actor.count('D'))
print(actor.count('d'))
print(actor.lower().count('d'))

print(actor.startswith('Da'))
print(actor.endswith('d'))
print(actor.startswith('M'))
print(actor.endswith('x'))

print(actor.index('royd'))
print(actor.find('royd'))

print(actor.find("Shatner"))

s = "fee fi fo    fum"
print(s.split())

ip = "10.99.8.17"
ip_bytes = ip.split('.')
print(ip_bytes)
print(ip_bytes[0])
print(ip[0])


s = "     All my exes live in Texas       "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print(s.replace(' ', ''))

s = "xxyxyxyyyAll my exes (Lexy) live in Texasyxxxxyyx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")

print(s.replace(' ', ''))

print(s.strip("xy").replace("Texas", "Moose Jaw"))


a = "Moose"
b = "Jaw"

print(a + b)
print(a + " " + b)
print("{} {}".format(a, b))
print(f"{a} {b}")







