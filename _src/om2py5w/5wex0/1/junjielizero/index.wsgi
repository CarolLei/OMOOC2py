# _*_ coding: utf-8 _*_


from bottle import*
import time  # 引入时间模块
import sae # 引入SAE模块，让网页在公共领域上线
import sae.kvdb # 引入KVDB模块
import sys
reload(sys)
sys.setdefaultencoding("utf8")

debug(True)


app = Bottle()
kv = sae.kvdb.Client()

@app.route('/write')
def write():
    
    return template('form.html') # 首次打开网页，显示登录页面，包含输入框

@app.route('/write', method='POST') 
def do_write():

    content = request.forms.get('content') # 输入框内容获取

    if content == 'r':
        index = kv.getkeys_by_prefix("c:") # key "c"指定设置

        number = sum(1 for _ in index) + 1 # 统计“c”值的数量

        k = 'c' + ':' + str(number) # 新“c” 创立

        return template('form2.html',content=content,kv=kv,k=k) # 打印文档

    elif content == '?':
        return template('form3.html' ,content=content) # 打印帮助

    elif content == 'delete':
        index = kv.getkeys_by_prefix("c:") # key "c"指定设置

        number = sum(1 for _ in index) + 1 # 统计“c”值的数量

        k = 'c' + ':' + str(number) # 新“c” 创立
        return template('delete.html',content=content,kv=kv,k=k)

    elif content == 'q':
        return template('form.html',content=content)

    else:
        date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        input = date + "\n" + content + "\n\n"

        index = kv.getkeys_by_prefix("c:") # key "c"指定设置

        number = sum(1 for _ in index) + 1 # 统计“c”值的数量

        k = 'c' + ':' + str(number) # 新“c” 创立

        kv.set(k, input) # 为新“c”设定value 

        value = kv.get(k)

        return template('form2.html',content=content,kv=kv,k=k) # 打印文档、输入内容，利用for……循环打印效果

application = sae.create_wsgi_app(app)