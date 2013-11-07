#to find the no lines in a pyfile
import sys
import os
def pyfiles(dir):
  files=os.listdir(dir)
  for f in files:
    if '.py' in f:
      print f,len(open(f).readlines())
pyfiles(sys.argv[1])

	
