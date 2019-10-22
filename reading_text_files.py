DATA_FILE = 'DATA/alice.txt'
f = open(DATA_FILE)
print(f)
f.close()

with open(DATA_FILE) as file_in:
    for line_no, raw_line in enumerate(file_in, 1):
        line = raw_line.rstrip()  # remove trailing \n
        if "Lizard" in line:
            print(line_no, line)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_contents = mary_in.read()
    print("cooked")
    print(all_contents)
    print("raw")
    print(repr(all_contents))
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    lines_with_nl = mary_in.readlines()
    print(lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    lines_without_nl = [line.rstrip() for line in mary_in]
    print(lines_without_nl)
print("-" * 60)

