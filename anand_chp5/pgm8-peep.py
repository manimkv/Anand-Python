# Program to implement a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

def peep(it):
   it1=list(it)
   p=it1[0]
   return p,it1
it = iter(range(5))
x,it1=peep(it)
print x,list(it1)



