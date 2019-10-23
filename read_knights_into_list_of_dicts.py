from pprint import pprint

file_name = 'DATA/knights.txt'

knight_data = []

with open(file_name) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data.append(
            (name, title, color, quest, comment)
        )

pprint(knight_data)