#Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get 

import urllib
import json
print 'loading............'
print json.response(urllib.urlopen('http://httpbin.org/get'))['origin']
