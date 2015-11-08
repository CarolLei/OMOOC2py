# _*_ coding: utf-8 _*_

import socket # 导入socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型s
s.bind(('127.0.0.1', 9999)) # 绑定端口

print 'Bind UDP on 9999...'
list =[]

while True:
	# 接收数据：
	data, addr = s.recvfrom(1024) # 接收1024字节，

	list.append(data)
	if len(list) == 1:
		continue

	else:
		print list[1]
		print type(list[1])


