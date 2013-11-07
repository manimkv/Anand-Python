#Write a function permute to compute all possible permutations of elements of a string

def permute(word):
  reslist=[]
  if len(word) == 1:
    reslist.append(word)
  else:
    for pos in range(len(word)):
      permutelist=permute(word[0:pos]+word[pos+1:len(word)])
      for item in permutelist:
        reslist.append(word[pos]+item)
  return list(set(reslist)) 
print permute('hello')
