#Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

import re
import urllib
def link(url):
  file=urllib.urlopen(url)
  list=re.findall('http://[\w\d\s\.-]+.html',file.read())
  list=['www.'+item[8:] for item in list]
  for item in list:
    print item
link('')
  
