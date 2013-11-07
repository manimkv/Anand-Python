#Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces and special characters are replaced by a hyphen.

import re
def make_slug(name):
  list=re.findall('\w+',name)
  list='-'.join(list)
  print list
make_slug('hello-- -world!')
