# _*_ coding: utf-8 _*_
# server 
 
import socket # 导入socket
import time  # 引入时间模块

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型s
s.bind(('127.0.0.1', 9999)) # 绑定端口

target = open('all.txt', 'a+') # 打开all.txt，并进入读取与追加状态
target.seek(0)

print 'Bind UDP on 9999...'
while True:
	# 接收数据：
  content, addr = s.recvfrom(1024) # 接收1024字节

  date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) # 计算时间（年月日时分秒） 
  target.write(date) # 写入时间
  target.write("\n") # 给写入空一行
  target.write(content) # 写入输入的日记内容
  target.write("\n\n") # 重新开一行，保持每行只有一条日记内容
  print 'Received content:', content

  '''
  print 'Received from %s:%s.' % addr
  '''
	
target.close()
