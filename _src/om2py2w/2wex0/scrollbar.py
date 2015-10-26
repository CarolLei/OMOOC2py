# _*_ coding: utf-8 _*_
from Tkinter import*

master = Tk() # 创建一个根窗口
scrollbar = Scrollbar(master, orient = VERTICAL) # 创建垂直方向滚动条，注意第一个参数
listbox = Listbox(master, yscrollcommand = scrollbar.set) # 创建带有y轴控制的滚动条


for item in range(0,5): # 输出列表元素，与本次任务吻合
	listbox.insert(END, item) 


scrollbar.config(command = listbox.yview) # 让滚动条在y轴上滚动
scrollbar.pack(side = RIGHT, fill = Y) # 将滚动条设置在右边
listbox.pack(side=LEFT,fill = BOTH, expand = 1) # 让文本框内容显示在左边

mainloop() # 消息循环，记得要输入
