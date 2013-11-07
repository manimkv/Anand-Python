# Program to count words in a file and print in descending order

import sys
filename=sys.argv[1]
def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
def read_words(filename):
    return open(filename).read().split()
frequency = word_frequency(read_words(filename))
def f(key):
    return frequency[key]
for key in sorted(frequency.keys(),key=f,reverse=True):
    print key, frequency[key]
