#Write a function group(list, size) that take a list and splits into smaller lists of given size.

import sys
def group(list,size):
  i,j,k=1,1,0
  for s in list:
    if len(list[(size*k):(size)*j])==0:
      sys.exit()
    else:
      l_i=list[(size*k):(size)*j]
      print l_i
      i,j,k=i+1,j+1,k+1
group([1,2,3,4,5,6,7,8,2,1,1,1,0],2)

