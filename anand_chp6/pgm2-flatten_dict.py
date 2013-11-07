#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

flatten={}
temp={}
def flatten_dict(d):
      temp={}
      for x,y in d.items():
         if isinstance(y,dict):
	    for i,j in y.items():
	       temp[x+'.'+i]=j
	    flatten_dict(temp)
         else:
	    flatten[x]=y
      return flatten

print flatten_dict({'a': 1, 'b':2, 'c': {'d':2, 'e': 3}, 'f': 4})

