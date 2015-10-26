# _*_ coding: utf-8 _*_
from Tkinter import* 

master = Tk() # 创建根窗口

listbox = Listbox(master) # 引入Listbox组件，创建消息窗口
listbox.pack() # 组块

listbox.insert(END, "a list entry") # 输出某值

for item in range(0,30): # 输出列表元素，与本次任务吻合
	listbox.insert(END, item)

mainloop() # 进入消息循环，否则无法显示界面

