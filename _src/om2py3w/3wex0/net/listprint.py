# _*_ coding: utf-8 _*_
#!/usr/bin/env python

# 打开文档
file = open('all.txt')
# 将文档内容生成列表
list = []
for line in file:
	list.append(line)
'''
print list # 测试效果
'''
'''
## 测试模块 
if 'client1\t' in list[0]:
	print 'yes'

else:
	print 'no'
'''

# 输入
content = raw_input(">  ")
content = content + '\t'

## 测试模块2
if content in list:
	print 'yes'

else:
	print 'no'



'''
# 打印全部
if content == 'all\t':
	file.seek(0)
	print file.read()
# 打印指定客户端记录
else:
	while True:
		for str in list:
		if content in list:
			i = list.index(content)
			print list[i:i+2]
			list.remove(content)

		else:
			print 'no client'
			break

print '****finish****'
file.close()
'''


	




