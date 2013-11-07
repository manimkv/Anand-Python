# Program to improve parse_csv function to parse all delimiters and comment indicators

import sys
def parse_csv(filename,d,c):
   return [x[:-1].split(d) for x in open(filename,'r').readlines() if x[0]!=c]
filename=sys.argv[1]
delim=raw_input("Enter the delimiter:")
comment=raw_input("Enter the comment indicator:")
print 'parse_csv(',filename,',',delim,',',comment,')=',parse_csv(filename,delim,comment)
