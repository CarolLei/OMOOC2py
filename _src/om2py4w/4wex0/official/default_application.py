# _*_ coding: utf-8 _*_
from bottle import Bottle, run, template # Bottle指定对象分配指定网址，可以不引入route(),引入模板

app = Bottle() # 给app变量分配一个网址,创建框架

@app.route('/hello') # 给app创建URL path
def hello():
	return "Hello World!"


if __name__ == '__main__':
	run(app, host='localhost', port=8080,debug=True) #注意运行要添加app变量