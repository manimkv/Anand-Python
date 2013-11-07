#Write a program reverse.py to print lines of a file in reverse order.

f=open('pgm17-lines.txt','r')
list=f.readlines()
s=[]
for line in list:
  s.insert(0,line)
print s
f.close()
fl=open('pgm17-res.txt','w')
fl.writelines(s)
fl=open('pgm17-res.txt','r')
print fl.read()
fl.close()
