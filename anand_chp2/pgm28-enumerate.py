#Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

s=[]
def enumerate(list):
  for l in list:
    s.append(list.index(l))
  print zip(s,list)
enumerate(['a','b','c','d'])
