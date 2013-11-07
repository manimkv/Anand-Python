#Write a python program zip.py to create a zip file. 

import sys
import zipfile
dir=sys.argv[1]
z=zipfile.ZipFile(dir,'w')
for i in range(2,len(sys.argv)):
  z.write(sys.argv[i])

