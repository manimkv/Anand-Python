# Program to implement center_alignment

import sys
filename=sys.argv[1]
f=open(filename,'r')
l=[]
p=[]
l.extend(f.readlines())
for i in l:
   p.append(len(i))
print max(p)
for i in l:
   if len(i)<max(p):
      print ' '*((max(p)-len(i))/2)+i
   else:
      print i
