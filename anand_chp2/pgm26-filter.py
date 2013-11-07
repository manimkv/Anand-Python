# Program to implement filter function 

def filter(f,a):
   return [x for x in a if f(x) is True]
def even(p):
   return p%2==0
l=[1,2,3,4]
print 'Original list',l
print filter(even,l)
