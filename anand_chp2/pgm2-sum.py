# Program to provide an implementation for built in function 'sum'

def sum(list):
   sum=0
   for i in list:
      sum=sum+i
   return sum
n=raw_input("Enter the length of list:")
list=[]
for i in range(int(n)):
   list.append(int((raw_input("Enter the element %d:" % i))))
print 'list =',list
print 'sum =',sum(list)

