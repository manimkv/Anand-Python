#Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys
n=sys.argv[1]
n=int(n)
lines=open(sys.argv[2]).readlines()
l=len(lines)
i=0
def split(lines,i):
  if len(lines)!=0:
    filename='file%d'%i
    f=open(filename,'w')
    if l%n==0:
      for j in range(n):
        f.write(lines[j])
      split(lines[n:],i+1)
    elif l<n or l%n!=0:
      print "it is not possible!!!\nTry another value of 'n'"
split(lines,i)
