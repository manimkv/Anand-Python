#Write a program extcount.py to count number of files for each extension in the given directory.

import os
import re
def extcount(filename):
  dict={}
  t=[]
  list=os.listdir(filename)
  ext=[re.findall('\.\w+',item) for item in list]
  for l in ext:
    l=l[0][1:]
    t.append(l)
  for word in t:
    dict[word]=dict.get(word,0)+1
  for key in sorted(dict):
    print key,'  ',dict[key]
extcount('extension')
