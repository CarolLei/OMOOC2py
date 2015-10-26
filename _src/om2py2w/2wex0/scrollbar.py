# _*_ coding: utf-8 _*_
from Tkinter import*

master = Tk()
scrollbar = Scrollbar(master, orient = VERTICAL)
listbox = Listbox(master, yscrollcommand = scrollbar.set)


for item in range(0,5): # 输出列表元素，与本次任务吻合
	listbox.insert(END, item)


scrollbar.config(command = listbox.yview)
scrollbar.pack(side = RIGHT, fill = Y)
listbox.pack(side=LEFT,fill = BOTH, expand = 1)

mainloop()
