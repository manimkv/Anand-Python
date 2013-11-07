#Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os
import sys
dir=sys.argv[1]
print dir
a='|--'
b='|   '
i=0
def dirtree(dir,i):
   filenames=os.listdir(dir)
   for filename in filenames:
      if not os.path.isdir(os.path.abspath(dir+'/'+filename)):
         if filename==filenames[-1]:	
            print b*i+'\--',filename
         else:
            print b*i+'|--',filename
      else:
         print b*i+'|--',filename
         dir=dir+'/'+filename
         dirtree(dir,i+1)

dirtree(dir,i)
