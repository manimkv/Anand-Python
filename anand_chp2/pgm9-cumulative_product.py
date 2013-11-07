# Program to implement cumulative product in list
def cumulative_product(l):
   a=[]
   p=1
   for item in l:
      p=p*item
      a.append(p)
   return a
n=raw_input("Enter the length of list:")
l=[]
for i in range(int(n)):
   l.append(int((raw_input("Enter the element %d:" % i))))
print 'Original list=',l
print 'cumulative_product(',l,')=',cumulative_product(l)
