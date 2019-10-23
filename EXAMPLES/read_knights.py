#!/usr/bin/env python
"""
Knight data example
"""
from pprint import pprint

def main():
    """
    Program starting point

    :return: None
    """
    knight_data = read_data()
    pretty_print(knight_data)
    print_knights(knight_data)
    print(get_item(knight_data, 'Arthur', 0))
    print(get_item(knight_data, 'Bedevere', 2))

def read_data():
    """
    Read knight data from file.

    :return:
    """
    knight_info = {}  # <1>

    with open("../DATA/knights.txt") as knights_in:
        for line in knights_in:
            (name, title, color, quest, comment) = line.rstrip('\n\r').split(":")
            knight_info[name] = title, color, quest, comment  # <2>
    return knight_info

def pretty_print(data):
    """
    Print the data in a readable format.

    :param data: dictionary of knight data
    :return: None
    """
    pprint(data)
    print()

def print_knights(data):
    """
    Display knights with their titles, one per line.

    :param data: dictionary of knight data
    :return: None
    """
    for name, info in data.items():
        print(info[0], name)
    print()

def get_item(data, knight, index):
    """
    Return one attribute of specified knight.

    :param data: dictionary of knight data
    :param knight: name of knight as string
    :param index: index to tuple of data
    :return: None
    """
    return data[knight][index]

if __name__ == '__main__': # am I a script?
    main()
