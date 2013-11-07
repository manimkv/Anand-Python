#Write a function cumulative_sum to compute cumulative sum of a list.

import re
list=raw_input('enter the list:')
l=re.findall('\w+',list)
s=[]
p=' '
for item in l:
  p=p+item
  s.append(p)
print s
