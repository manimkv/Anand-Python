# Program to print a file in reverse order

import sys
filename=sys.argv[1]
f=open(filename,'r')
l=[]
l.extend(f.readlines())
l.reverse()
for i in l:
  print i
