#program to map a function over nested list

def treemap(fun,lis):
   for i in range(len(lis)):
      if isinstance(lis[i],list):
         treemap(fun,lis[i])
      else:
	 sqr=fun(lis[i])
	 lis.remove(lis[i])
	 lis.insert(i,sqr)
   return lis

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
	
