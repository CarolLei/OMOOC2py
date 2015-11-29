# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup 
import sys
reload(sys)
sys.setdefaultencoding("utf8")

def write(content,tag):

  value = {'content': content,'tag':tag}  # 模拟网页手动输入，用字典方式传递
  url = "http://junjielizero.sinaapp.com/write"
  r = requests.post(url, data=value)
  soup = BeautifulSoup(r.text, "html.parser")
  for i in soup.find_all('pre'):
    print i.get_text()

tag = raw_input("tag: ")
content = raw_input("content: ")

if content == '?':
    print '寻求帮助，请输入？'
    print '退出笔记，请按CTRL+C'
    print '同步当前主题笔记，请按r'
    print '清除当前主题笔记，请输入delete'
    print '切换主题，请输入q'

else:
  write(content,tag)

while True:

    content = raw_input("content: ")

    if content == '?':
        print '寻求帮助，请输入？'
        print '退出笔记，请按CTRL+C'
        print '同步当前主题笔记，请按r'
        print '清除当前主题笔记，请输入delete'
        print '切换主题，请输入q'

    elif content == 'q':
      tag = raw_input("tag: ")
      content =raw_input("content: ") 
      write(content,tag)

    else:
      write(content,tag)
