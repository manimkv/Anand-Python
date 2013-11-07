# Program to find anagrams in a list

def anagrams(l):
   s=[]
   s.append([l[0]])
   for i in range(1,len(l)):
      flag=0
      for j in range(len(s)):
         if sorted(list(l[i]))==sorted(list(s[j][0])):
	    s[j].append(l[i])
	    flag=1
	    break
      if flag==0:
         s.append([l[i]])
   return s
	
print anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node','pous','oned','lop'])


