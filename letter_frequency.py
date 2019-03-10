#This program reads a file and determines the most frequent letter in the English language
#In this case the U.S. constitution. Ather files can be used to determine the most frequently used letter

import matplotlib.pyplot as plt
import string

data = open("sonnets.txt", "r").read()

#create an empty dictionary to store and count each alphabet the appears in the dictionary
letter_counts = {}
#for every letter initialize the dictionary with zero
for char in string.ascii_lowercase:
    letter_counts[char] = 0

#check to see if the letter in the constitution appears in the ASCII letters. If so increment that letters count
for char in data:
    char = char.lower()
    if char in string.ascii_lowercase:
        letter_counts[char] += 1

frequencies = letter_counts.items()
labels = []
counts = []
for letter, count in sorted(frequencies):
    labels.append(letter)
    counts.append(count)

#'xlocations' is a list of numbers from 0 to the number of frequencies we are plotting - which is the 26 letters
xlocations = range(len(frequencies))
#width is the width of the bar chart
width = 0.5
#calculate where along the x-axis the ticks for each bar should go
plt.xticks([i + width/2 for i in xlocations], labels)
plt.bar(xlocations, counts, width=width)
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter Frequencies in Shakespear's Sonnet")
plt.show()
