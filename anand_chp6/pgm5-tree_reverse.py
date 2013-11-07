#Write a function tree_reverse to reverse elements of a nested-list recursively.

def tree_reverse(lis):
   lis.reverse()
   for i in lis:
      if isinstance(i,list):
         tree_reverse(i)			
   return lis
print tree_reverse([[1, 2], [3, [4, 5]], 6])
		

