#!/usr/bin/env python

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]  # grab 1st letter of word

        if first_letter not in letter_counts: # is not a key
            letter_counts[first_letter] = 0 # initialize it

        letter_counts[first_letter] += 1  # increment count

for letter, count in letter_counts.items():
    print(letter, count)
