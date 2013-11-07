#Write a function extsort to sort a list of files based on extension.

def extsort(l):
  l.sort(key=lambda x:x.split('.')[1])
  print l
extsort(['a.c','a.py','b.c','bar.txt','foo.txt','x.c'])
