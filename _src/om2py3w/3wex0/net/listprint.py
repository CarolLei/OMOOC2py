# _*_ coding: utf-8 _*_
#!/usr/bin/env python

file = open('all.txt','r+')

list = []
for line in file:
	list.append(line)

content = 'client1\n'

while True:
	if content in list:
		i = list.index(content)
		print list[i]
		print list[i+1]
		print list[i+2]
		list.remove(content)

	else:
		break

print 'finish'