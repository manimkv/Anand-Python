# Program to implement the unix commands grep

import sys
filename=sys.argv[1]
f=open(filename,'r')
l=[]
l.extend(f.readlines())
s=raw_input('Enter the string:')
for i in l:
   if s in i:
      print i
