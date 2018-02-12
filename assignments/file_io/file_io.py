#!/usr/bin/env python3

# Read the file meditations.txt into a string called meditations
with open("meditations.txt") as f:
    meditations = f.read()

# Use the .splitlines() method to split that string into a list of lines called meditation_list
meditation_list = meditations.splitlines()

# Write the number of words in each line to a file called word_count.txt
# Make sure each number apppears on a new line.
with open("word_count.txt", "w") as f:
    for line in meditation_list:
        f.write(str(len(line.split())) + '\n')

