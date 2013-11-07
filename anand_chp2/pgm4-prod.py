# Program to provide an implementation for finding product of list elements

def product(l):
   p=1
   for i in l:
   p=p*i
   return p
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
   l.append(int((raw_input("Enter the element %d:" % i))))
print 'list=',l
print 'Product =',product(l)

