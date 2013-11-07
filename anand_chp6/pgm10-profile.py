#implement a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it

import time
def fib(n):
   if n is 0 or n is 1:
      return 1
   else:
      return fib(n-1)+fib(n-2)

def profile(fun):
   def g(x):
      t=0
      start=time.time()
      v=fun(x)
      t=time.time()-start
      return str(t)+'  sec'
   return g

fib = profile(fib)
print fib(26)
