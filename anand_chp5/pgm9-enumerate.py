#The built-in function enumerate takes an iteratable and returns an iterator over pairs (index, value) for each value in the source.

import itertools
def my_enumerate(list):
  return (itertools.izip(range(len(list)),list))
print list(my_enumerate(['a','b','c','d']))
for i,c in my_enumerate(['a','b','c','d']):
   print i,c
