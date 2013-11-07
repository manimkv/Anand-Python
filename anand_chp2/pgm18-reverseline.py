# Program to print lines of a file in reverse order

import sys
filename=sys.argv[1]
f=open(filename,'r')
l=[]
l.extend(f.readlines())
for i in l:
  print i[::-1]
