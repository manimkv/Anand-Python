#Write a function dups to find all duplicates in the list.

import re
list=raw_input('enter the list:')
p=[]
s=[]
r=[]
l=re.findall('\d+',list)
for n in l:
  if n in s:
    p.append(n)
    if n not in r or len(r)==0:
      r.append(n)
  else:
    s.append(n)
print r    
