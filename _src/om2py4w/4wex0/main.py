# _*_ coding: utf-8 _*_
from bottle import*
import time  # 引入时间模块


@route('/write')
def write():
    
    return template('form.html') # 首次打开网页，显示登录页面，包含输入框

@route('/write', method='POST') 
def do_write():

    content = request.forms.get('content') # 输入框内容获取

    if content == 'r':
        file = open('all.txt', 'r')
        return template('form2.html', file=file,content=content) # 打印文档

    elif content == '?':
        return template('form3.html' ,content=content) # 打印帮助

    else:
        file = open('all.txt', 'a+') 
        file.seek(0)
        date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        file.write(date + "\n" + content + "\n\n")
        file.seek(0)
        return template('form2.html', file=file,content=content) # 打印文档、输入内容，利用for……循环打印效果

if __name__ == '__main__':
    debug(True) # debug
    run(host='localhost', port=8090, reloader=True) 
