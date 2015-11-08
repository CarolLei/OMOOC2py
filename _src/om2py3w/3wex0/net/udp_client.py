# _*_ coding: utf-8 _*_

import socket # 导入socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型s
for data in ['Michael', 'Tracy']:
	# 发送数据：
	s.sendto(data, ('127.0.0.1', 9999))
	# 接收数据：
s.close() 


