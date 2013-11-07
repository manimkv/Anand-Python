#Write a function unique to find all the unique elements of a list.

import re
def unique(list,key):
 # l=re.findall('\w+',list)
  s=[]
  for key in list:
    if key not in s or len(s)==0:
      s.append(key)
  print s
unique(['Python,jAvA,ruby,java,perl,python,java'],key=lambda x:x.lower())

