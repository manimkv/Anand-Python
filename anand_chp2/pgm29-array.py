# Program create a two dimensional array using list

def array(a,b):
   return [[None]*b for i in range(a)]
m=int(raw_input('Enter the number dimensions element 1:'))
n=int(raw_input('Enter the number dimensions element 2:'))
print 'array(',m,',',n,')=',array(2,3)
s=array(2,3)
