#Write a python function parse_csv to parse csv (comma separated values) files.

import re
res=[]
def parse_csv(file):
  f=open(file,'r')
  txt=f.readlines()
  for l in txt:
    s=re.findall('\w+',l)
    res.append(s)
  print res
parse_csv('a.csv')
