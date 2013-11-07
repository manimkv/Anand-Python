import os
import re
def extcount(filename):
  dict={}
  list=os.listdir(filename)
  ext=[re.findall('.\w+',item) for item in list]
  ext=[item[1:] for item in ext]
  for word in ext:
    dict[word]=dict.get(word,0)+1
  for key in sorted(dict):
    print key+' '+dict[key]

