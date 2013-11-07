#Write a function lensort to sort a list of strings based on length.

def len_sort(list):
  list.sort(key=lambda x:len(x))
  print list
len_sort(['python','perl','java','c','java','ruby','haskell','python'])

