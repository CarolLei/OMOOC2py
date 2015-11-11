# _*_ coding: utf-8 _*_
from bottle import*
import time  # 引入时间模块
import socket



@route('/write')
def write():
    
    return template('form.html')

@route('/write', method='POST') 
def do_write():

    content = request.forms.get('content') # 用户名

    if content == 'r':
        file = open('all.txt', 'r')
        return template('form2.html', file=file,content=content)

    elif content == '?':
        return template('form3.html' ,content=content)

    else:
        file = open('all.txt', 'a+') 
        file.seek(0)
        date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        file.write(date + "\n" + content + "\n\n")
        file.seek(0)
        return template('form2.html', file=file,content=content)




if __name__ == '__main__':
    debug(True) # debug
    run(host='localhost', port=8090, reloader=True) 

    #