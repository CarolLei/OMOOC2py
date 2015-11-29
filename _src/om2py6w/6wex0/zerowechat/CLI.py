# _*_ coding: utf-8 _*_

import requests
import time 
import sys 
reload(sys)
sys.setdefaultencoding("utf8")

import xml.etree.ElementTree as ET
import urllib2
import json

headers = {'content-type':'application/xml'}

def echo(content):

    # 改ToUserName, FromUserName

    echostr="""<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>    
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    <MsgId>1234567890123456</MsgId>
    </xml>"""%('a' ,'b',int(time.time()),"text",content)


    
    url = "http://localhost:8080/echo"
    r = requests.post(url, data=echostr,headers=headers)
    print r.text


while 1:

	content =raw_input("content: ")
	echo(content)


if __name__ == '__main__':
	echo()