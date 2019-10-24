#!/usr/bin/env python
from temperature import c2f

for c in -40, 0, 37, 100:
    f = c2f(c)
    print("{} C is {} F".format(c, f))
