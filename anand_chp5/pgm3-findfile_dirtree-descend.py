#Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os
import sys
tree=''
def findfile(dir,dirt):
  global tree
  files=os.listdir(dir)
  
  for f in files:
    print os.path.abspath(dir+'/'+f)
    if os.path.isdir(os.path.abspath(dir+'/'+f)):
      if f==dirt:
        tree=os.path.abspath(dir+'/'+f)
      else:
	findfile(dir+'/'+f,dirt)
findfile(sys.argv[1],sys.argv[2])		
print 'specified directory found at ',tree			
