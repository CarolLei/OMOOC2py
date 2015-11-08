# _*_ coding: utf-8 _*_
# client2

import socket # 导入socket

# 打印历史
history = open('all.txt')
print history.read()
history.close()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 


while True:  # 利用while循环实现重复调用脚本效果
  content = raw_input("content: ") # 输入日记内容

  if content == '?':
    print '打印当前，帮助输入？'
    print '退出笔记，请按CTRL+C'
    print '同步全部笔记历史，请按r'
    print '打印客户端1笔记历史，请按r1'
    print '打印客户端2笔记历史，请按r2'

  elif content == 'r':#打印所有客户端记录
    now = open('all.txt')
    print now.read()
    now.close()

  elif content == 'r1': # 打印客户端1记录
    now = open('client1.txt')
    print now.read()
    now.close()

  elif content == 'r2': # 打印客户端2记录
    now = open('client2.txt')
    print now.read()
    now.close()

  else: # 目的在于输送标示的内容，这里用client1作为标识，给服务端两个数据（client1,content）,均为string
    list = ['client2']
    list.append(content)
    for data in list:
      s.sendto(data,('127.0.0.1', 9999))

s.close() 
