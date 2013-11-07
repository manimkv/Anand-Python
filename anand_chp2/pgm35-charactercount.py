# Program to count characters and their frequencies in a file

import sys
filename=sys.argv[1]
def char(filename):
	return open(filename).read()
def char_frequency(char):
	frequency = {}
	for i in range(len(char)):
		if char[i]!='\n':
			frequency[char[i]]=frequency.get(char[i], 0)+1
	return frequency
frequency=char_frequency(char(filename))
def f(key):
    return frequency[key]
for key in sorted(frequency.keys(),key=f,reverse=True):
    print key, frequency[key]


