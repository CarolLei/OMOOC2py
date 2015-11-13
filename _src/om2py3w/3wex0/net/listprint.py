# _*_ coding: utf-8 _*_
#!/usr/bin/env python

def output():

	for content in str:

		i = str



file = open('all.txt')

list = []
for line in file:
	list.append(line)
'''
print list

if 'client2' in list[0]:
	print 'yes'

else:
	print 'no'
'''
content = raw_input(">  ")


if content == 'all':
	file.seek(0)
	print file.read()

else:
	while True:
		for str in list:

			if content in str:



'''
else:
	while True:
		if content in list:
			i = list.index(content)
			print list[i]
			print list[i+1]
			print list[i+2]
			list.remove(content)

		else:
			print 'no client'
			break

print '****finish****'
file.close()
'''
if 