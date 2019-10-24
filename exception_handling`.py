#!/usr/bin/env python
file_name = 'DATA/medicine_hat.txt'

try:
    with open(file_name) as mh_in:
        pass
except OSError as err:
    print("Uh-oh:", err)


values = 5, 8, 4, 0, 9, 'pine marten', 11, 2

for v in values:
    try:
        result = 21 / v
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(result)
print()

for x in  123, "abc", "456", 5.93, "   8383  ", "  wombat  ":
    try:
        i = int(x)
    except ValueError as err:
        print(err)
        exit()
    else:
        print(i)
    finally:
        print("moose!")









