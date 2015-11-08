# _*_ coding: utf-8 _*_
#!/usr/bin/env python

import uniout
from pprint import pprint

file = open('all.txt','a+')
file.seek(0)

list = ['a']

file.write(list)

print file.read()

file.close()