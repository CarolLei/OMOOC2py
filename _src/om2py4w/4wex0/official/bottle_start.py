# _*_ coding: utf-8 _*_
# 
from bottle import route, run, template, debug, get,post, request
# 从bottle引入连接route()，运行run(),引入模块，get,post,request用于https

@route('/hello') # URL path,可以创建多个path
def hello():   # 网页程现的内容
	return "Hello World!"  # 返回显示的内容，注意没有print


@route('/hollo/<name>') # 在运行网址时，<name>可改名字
def hollo(name):
	return "中文 %s" % name # 可在网页上显示输入的name

@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@route('/login', method='POST') # method 指定协议行为
def do_login():
    username = request.forms.get('username') # 用户名
    password = request.forms.get('password') # 密码
    print "srv.got:", username, password # 对公网站进行内部变量运行
    if username:
        return template("<p>成功!<hr/>{{ name }}<p>", name=username) # 登陆后的页面内容，模板一种，具体请尝试


@route('/')
def root():
    return '''Hollo there!
    demo v15.11.4.0808
        usage ~ Hummm Orz...

    '''

if __name__ == '__main__':
	debug(True) # debug
	run(host='localhost', port=8080, reloader=True) # 运行服务端，Port8080，自动重启服务区reloader = True
