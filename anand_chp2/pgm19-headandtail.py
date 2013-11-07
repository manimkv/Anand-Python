# Program to implement the unix commands head and tail

import sys

def head(l):
   if len(l)>10:
      for i in range(10):
         print l[i]
   else:
      for i in range(len(l)):
         print l[i]

def tail(l):
    if len(l)>10:
       for i in range(len(l)-10,len(l)):
          print l[i]
    else:
       for i in range(len(l)):
          print l[i]
filename=sys.argv[1]
f=open(filename,'r')
l=[]
l.extend(f.readlines())
print '____Head_____'
head(l)
print '_____Tail____'
tail(l)
