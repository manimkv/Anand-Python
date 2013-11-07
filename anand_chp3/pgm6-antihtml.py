#Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.

import re
import os
import urllib
import sys
url=sys.argv[1]
if url[-1]=='/':
   basename='index.html'
else:
   basename=url.split('/')[-1]
print 'Saving  ',url,'  as ',basename
urllib.urlretrieve(url,os.getcwd()+'/'+basename)
f=open(basename,'r')
strings = re.findall(r'>[^<]+<', f.read())
for i in strings:
   print i[1:-1]

