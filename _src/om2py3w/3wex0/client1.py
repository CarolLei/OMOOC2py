# _*_ coding: utf-8 _*_
# client1

from sys import argv 
import socket # 导入socket
import time  # 引入时间模块

history = open('all.txt')
print history.read()
history.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型


while True:  # 利用while循环实现重复调用脚本效果
  content = raw_input("content: ") # 输入日记内容

  if content == '?':
  	print '打印当前，帮助输入？'
  	print '退出笔记，请按CTRL+C'
  	print '同步笔记历史，请按r'

  elif content == 'r':
    now = open('all.txt')
    print now.read()
    now.close()

  else:
  	s.sendto(content, ('127.0.0.1', 9999))

s.close() 
