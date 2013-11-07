#Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet      equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet

n=raw_input('enter triplet value:')
m=int(n)
a=[(x,y,z) for x in range(1,m) for y in range(x,m) for z in range(y,m) if x+y==z]
print a
