# _*_ coding: utf-8 _*_

from Tkinter import*
from ScrolledText import*
import time  # 引入时间模块

from sys import argv 
script = argv # 本地已有demo2.py, test.txt(已存在）

class Application(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self): # 创建组件（包括文本框、输入框、）
		# 创建文本框
		self.text = ScrolledText(self) 
		target = open('test.txt', 'a+')  # 打开test.txt，并进入读取与追加状态
		target.seek(0)
		self.text.insert(END, target.read()) # 打印文档记录
		self.text.pack(side= BOTTOM)

		# 创建输入框并可以输入 
		self.content = StringVar(self)
		self.enter = Entry(self,textvariable=self.content)
		self.enter.bind("<Return>", self.write)  # bind第二参数可以调用函数
		self.enter.pack(side=TOP,fill = X)

	def write(self,target): # 输入内容后，按<Return>消失，同时内容一能保存到txt文档，二能在文本框显示
		content = self.content.get()
		target = open('test.txt', 'a+')  # 打开test.txt，并进入读取与追加状态
		date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) # 计算时间（年月日时分秒） 
		target.write(date) # 写入时间
		target.write("\n") # 给写入空一行
		target.write(content) # 写入输入的日记内容
		target.write("\n\n") # 重新开一行，保持每行只有一条日记内容
		target.close()
		self.text.insert(END,date)
		self.text.insert(END,"\n")
		self.text.insert(END,content) # 在文本框显示
		self.text.insert(END,"\n\n")
		self.text.see(END) # 指定位置
		self.enter.delete(0,END) # 清除输入框内容，需由bind的Return激活

root = Tk()
root.title('Mydiary')
app = Application(master = root)
app.mainloop()
