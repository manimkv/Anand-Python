#Write a program to print each line of a file in reverse order.

import re
f=open('pgm18-line.txt','r')
list=f.readlines()
s=[]
res=[]
for line in list:
  split=re.findall('[\w\';,.]+',line)
  for spl in split:
    s.insert(0,spl)
  p=' '.join(s)
  s=[]
  res.insert(0,p)
f.close()
l=open('pgm18-res.txt','w')
l.writelines(res)
l.close()
l=open('pgm18-res.txt','r')
print l.read()
l.close()
