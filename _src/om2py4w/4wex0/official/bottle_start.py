# _*_ coding: utf-8 _*_
from bottle import route, run, template, debug# 从bottle引入连接route()，运行run(),引入模块

@route('/hello') # URL path,可以创建多个path
def hello():   # 网页程现的内容
	return "Hello World!"  # 返回显示的内容，注意没有print


@route('/hollo/<name>') # 在运行网址时，<name>可改名字
def hollo(name):
	return "中文 %s" % name # 可在网页上显示输入的name

if __name__ == '__main__':
	debug(True) # debug
	run(host='localhost', port=8080, reloader=True) # 运行服务端，Port8080，自动重启服务区reloader = True
