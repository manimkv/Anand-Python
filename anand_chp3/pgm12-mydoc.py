#Write a program mydoc.py to implement the functionality of pydoc. 

import sys
__import__(sys.argv[1])
print 'Help on module ',sys.argv[1],':'
print '\n\nDESCRIPTION\n\n'
print sys.argv[1].__doc__
print '\n\nFUNCTIONS\n\n'
for i in dir(sys.argv[1]):
  print i,'()'

	
