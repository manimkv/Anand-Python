# Program to compute all words formed by a single mutation in given word

alph='abcdefghijklmnopqrstuvxwyz'
alphlist=[alph[i] for i in range(len(alph))]

def inserting(word):
  l_1=[]
  l_2=[]
  wordlist=[word[j] for j in range(len(word))]
  for let in alphlist:
    for k in range(len(wordlist)+1):
      l_1.extend(wordlist)
      l_1.insert(k,let)
      s_1=''.join(l_1)
      l_2.append(s_1)
      l_1=[]
  return l_2    


def deleting(word):
  wordlist=[word[j] for j in range(len(word))]
  d=[]
  l_3=[]
  for i in range(len(wordlist)):
    d.extend(wordlist)
    del wordlist[i]
    s_2=''.join(wordlist)
    l_3.append(s_2)
    wordlist=d
    d=[]       
  return l_3


def replacing(word):
  d=[]
  l_4=[]
  wordlist=[word[j] for j in range(len(word))]
  for let in alphlist:
    for i in range(len(wordlist)):
      d.extend(wordlist)
      del d[i]
      d.insert(i,let)
      s_2=''.join(d)
      l_4.append(s_2)
      d=[]
  return l_4


def swaping(word):
  d=[]
  l_5=[]
  wordlist=[word[j] for j in range(len(word))]
  for i in range(len(wordlist)):
    if i!=len(wordlist)-1:
      d.extend(wordlist)
      d[i],d[i+1]=d[i+1],d[i]
      s_3=''.join(d)
      l_5.append(s_3)
      d=[]
  return l_5


def mutate(word):
  print 'INSERTING..........\n\n',inserting(word),'\n\n'
  print 'DELETING...........\n\n',deleting(word),'\n\n'
  print 'REPLACING..........\n\n',replacing(word),'\n\n'
  print 'SWAPING...........\n\n',swaping(word),'\n\n'
  print '<<<<<<<<<<<MUTATING>>>>>>>>>\n\n',inserting(word)+deleting(word)+replacing(word)+swaping(word)

mutate('hello')
