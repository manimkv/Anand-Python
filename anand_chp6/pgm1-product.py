#Implement a function product to multiply 2 numbers recursively using + and - operators only.

def product(x,y):
   if x<0 and y<0:
      return abs(x)+product(abs(x),abs(y)-1)
   elif x<0 and y>0:
      return x+product(x,abs(y)-1)
   elif x>0 and y<0:
      return -x+product(-x,abs(y)-1)
   elif x==0 or y==0:
      return 0
   else:
      return x+product(x,y-1)

print product(0,6)
     
