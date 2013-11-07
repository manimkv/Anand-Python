# Program to sort values of a dictionary based on a key

def valuesort(d):
   return [d[x] for x in sorted(d.keys())]
print valuesort({'x': 1, 'y': 2, 'a': 3})
