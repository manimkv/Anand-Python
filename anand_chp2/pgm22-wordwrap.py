# Program to wrap length of line by a width without breaking a word

import sys
filename=sys.argv[1]
c=int(sys.argv[2])
f=open(filename,'r')
l=[]
l.extend(f.readlines())
for i in l:
   new=i
   while len(new)>c :
      if new[c-1]!=' ':
         for j in range(c-1):
            if new[:c-1][-j]==' ':
               print new[:c-1+(-j)]
               break;
         new=new[c-1+(-j):]
      else:
         print new[:c-1]
         new=new[c-1:]
   print new[:-1]
