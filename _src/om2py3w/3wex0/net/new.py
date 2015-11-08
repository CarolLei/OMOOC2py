# _*_ coding: utf-8 _*_
#!/usr/bin/env python

import uniout
from pprint import pprint


file = open('all.txt','r+')

list = []
for line in file:
	list.append(line)

print list

for line in list:
	print line








