#Write a function to compute the number of python files in a specified directory recursively.

import os
import sys
def count(files):
  return [file for file in files if '.py' in file]
files=os.listdir(sys.argv[1])
pyfiles=count(files)
print len(pyfiles)

	

	
