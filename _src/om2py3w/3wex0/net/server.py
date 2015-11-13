# _*_ coding: utf-8 _*_
# server 
 
import socket # 导入socket
import time  # 引入时间模块

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建socket，UDP类型s
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999)) # 绑定端口

# 选择性打印
def reyn(content):

  k = {'client1':client1, 'client2':client2}

  if index in k:
    file = k.get(index)
    file.seek(0)
    file.write(index + "\n" + date + "\n" + content + "\n\n")
    file.close()

list = []

print 'Bind UDP on 9999...'
while True:

	# 接收数据：
  data, addr = s.recvfrom(1024) # 接收数据、地址

  list.append(data) # 由于接收的数据，有两次，第一次是标识，第二次是标识+输入的内容
  if len(list) == 1: # 放弃第一次接收，因为只有没有接收输入的内容

    continue

  else: 

    content = list[1]  # 输入的内容
    index = list[0] # 标识
    
    # 输入到完整的历史记录文档
    all = open('all.txt','a+')
    all.seek(0)

    date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
    all.write(index + " " + date + "\n" + content + "\n\n")

    # 在服务端观察输入效果
    print index + "\n"
    print date + "\n"
    print content + "\n\n"

    # 打开两个客户端文件
    client1 = open('client1.txt','a+')
    client2 = open('client2.txt','a+')

    reyn(content) # 选择性同步

    all.close()
    client1.close()
    client2.close()
    
    # 清除列表内容，否则下次输入，不能接收新的数据
    del list[:]


