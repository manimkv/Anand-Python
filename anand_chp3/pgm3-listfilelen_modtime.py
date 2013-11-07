# Write a program to list all the files in the given directory along with their length and last modification time

import os
def list(dir):
  file=os.listdir(dir)
  for item in file:
    print item,' ',len(item),' ',os.stat(os.path.abspath(os.path.join(dir,item)))[7]
list('/home/mani/test')
