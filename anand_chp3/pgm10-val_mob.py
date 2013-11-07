#Write a regular expression to validate a phone number.

import re
def val_mob_no(num):
  list=re.findall('\d{1,10}',num)
  if len(list[0])==10 and len(list[:1]==0):
    print 'Your mobile number is valid'
  else:
    print 'sorry! Your mobile number is not valid'
val_mob_no('98965425')
