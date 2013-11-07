# Program to implement unique function using sets

def unique(l):
 return list(set(l))
print 'Testing phase--Use integer list' 
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
 l.append(int((raw_input("Enter the element %d:" % i))))
print 'Origial list=',l
print 'unique(',l,')=',unique(l)
