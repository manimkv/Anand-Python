# Program to implement zip function using list comperhension

def zip(a,b):
   if len(a)<len(b):
      return [(a[i],b[i]) for i in range(len(a))]
   else:
      return [(a[i],b[i]) for i in range(len(b))]
l=[1,2,3,4]
s=['a','b','c']
print 'Original lists',l,' ',s
print 'zip(',l,',',s,')=',zip(l,s)
