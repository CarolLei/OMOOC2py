# _*_ coding: utf-8 _*_


from bottle import*
import time # 引入时间模块,密码模块
import sae # 引入SAE模块，让网页在公共领域上线
import sae.kvdb # 引入KVDB模块
import sys
reload(sys)
sys.setdefaultencoding("utf8")

debug(True)


app = Bottle()
kv = sae.kvdb.Client()
taglist = []

# 保存tag
def savetag(tag):

    tagindex = kv.getkeys_by_prefix('s#')

    for k in sorted(tagindex,key=lambda x:int(x.split('#')[-1])):
        taglist.append(kv.get(k))

    if tag is None:

        tag = taglist[-1]

        return tag     

    else:

        if tag in taglist:

            return tag

        else:

            tagnumber = sum(1 for _ in tagindex) + 1 

            c = 's#' + str(tagnumber)

            kv.set(c, tag)

            return tag


# 日记运行
@app.route('/')
def write():
    
    return template('form.html') # 首次打开网页，显示登录页面，包含输入框

@app.route('/write', method='POST') 
def do_write():

    content = request.forms.get('content') # 输入框内容获取
    tag = request.forms.get('tag') # 获取tag内容
    

    if content == 'r':

        tag = savetag(tag)

        key = tag + ':'

        index = kv.getkeys_by_prefix(tag) # key "c"指定设置

        number = sum(1 for _ in index)

        k = key + str(number)

        return template('form2.html',content=content,kv=kv,k=k,key=key,tag=tag,number=number) # 打印文档

    elif content == '?':
        return template('form3.html' ,content=content) # 打印帮助

    elif content == 'delete':

        tag = savetag(tag)

        key = tag + ':'

        index = kv.getkeys_by_prefix(key) # key "c"指定设置

        number = sum(1 for _ in index)  # 统计“c”值的数量

        k = key + str(number) # 新“c” 创立
        return template('delete.html',content=content,kv=kv,k=k,key=key,tag=tag)

    elif content == 'q':
        return template('form.html',content=content)

    else:
        date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())
        input = date + "\n" + content + "\n\n"

        tag = savetag(tag)

        key = tag + ':'

        index = kv.getkeys_by_prefix(key)

        number = sum(1 for _ in index) + 1 # 统计“c”值的数量

        k = key + str(number) # 新“c” 创立

        kv.set(k, input) # 为新“c”设定value 

        return template('form2.html',content=content,kv=kv,k=k,tag=tag,key=key,number=number) # 打印文档、输入内容，利用for……循环打印效果

application = sae.create_wsgi_app(app)

if __name__ == "__main__":

    debug(True)

    run(app, host='127.0.0.1',port=8080,reloader=True)