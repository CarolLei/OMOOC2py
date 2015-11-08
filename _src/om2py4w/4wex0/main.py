# _*_ coding: utf-8 _*_
from bottle import*

'''
file = open('all.txt', 'r+')
print type(file.read())
'''

'''打印所有记录'''
@route('/h')
def history():

	file = open('all.txt', 'r+')
	return "%s" % file.read()



if __name__ == '__main__':
	debug(True) # debug
	run(host='localhost', port=8080, reloader=True) # 运行服务端，Port8080，自动重启服务区reloader = True
