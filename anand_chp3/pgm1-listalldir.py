#Write a program to list all files in the given directory.

import os
def listdir(dir):
  filename=os.listdir(dir)
  print filename
listdir('/home/mani/test')
