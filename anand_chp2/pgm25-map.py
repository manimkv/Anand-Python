# Program to implement the built in function 'map'

def map(f,l):
   return [f(x) for x in l] 
def square(p):
   return p*p
l=[1,2,3,4]
print 'Original list',l
print map(square,l)
