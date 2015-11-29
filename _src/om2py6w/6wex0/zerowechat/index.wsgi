# _*_ coding: utf-8 _*_

from bottle import*
import time,hashlib,os  # 引入时间模块,密码模块
import sae # 引入SAE模块，让网页在公共领域上线
import sae.kvdb # 引入KVDB模块
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import xml.etree.ElementTree as ET
import urllib2
import json

debug(True)


app = Bottle()
kv = sae.kvdb.Client()
list = []

# 微信验证
@app.get('/echo')
def checkSignature():
    response.content_type = 'content_type:text'

    token = "111111"
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        return echostr
    else:
        return "wws: indentify error"

# 微信接收消息
def parse_msg():
    recvmsg=request.body.read()
    root=ET.fromstring(recvmsg)
    msg={}
    for child in root:
        msg[child.tag]=child.text
    return msg

# 微信回复消息
@app.post('/echo')
def response_msg():

    msg=parse_msg()
    recv = msg['Content']
    content = reply(recv)


    echostr="""<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>"""%(msg['FromUserName'] ,msg['ToUserName'],int(time.time()),"text",content)


    return echostr

# 回复设计
def reply(recv):
    

    if recv == 'delete':

        key = 'hilde' + ':'

        k = key

        for k in kv.getkeys_by_prefix(key):
            kv.delete(k)

        index = kv.getkeys_by_prefix(key)

        output = 'delete'
        number = sum(1 for _ in index) 

        output = ('\n').join(['delete all' ,'共搜集'+str(number) +'条笔记'])

        return output

    elif recv == 'h':

        output = ('\n').join(['目前支持以下命令:','m..记录笔记','h: 寻求帮助','s: 查看历史'])

        return output


    elif recv == 's':

        del list[:]

        key = 'hilde' + ':' # 待修改

        index = kv.getkeys_by_prefix(key)
        number = sum(1 for _ in index) 

        k = key + str(number)
        for k in sorted(kv.getkeys_by_prefix(key),key=lambda x:int(x.split(':')[-1])):
            list.append(kv.get(k))

        output = '\n'.join(list)

        return output

    elif recv.startswith("m..") :

        recv = recv.split('m..')[-1]

        key = 'hilde' + ':' # 待修改

        index = kv.getkeys_by_prefix(key)
        number = sum(1 for _ in index) + 1 

        k = key + str(number)

        kv.set(k, recv)

        output = 'Hi' + ':' + '共搜集'+ str(number) + '条笔记' 

        return output

    else:
        output = '\n'.join(['输入有误','目前支持以下命令:','m..记录笔记','h: 寻求帮助','s: 查看历史'])

        return output

if __name__=="__main__":
    debug(True)
    run(app,host='127.0.0.1',port=8080,reloader=True)

else:
    application = sae.create_wsgi_app(app)



