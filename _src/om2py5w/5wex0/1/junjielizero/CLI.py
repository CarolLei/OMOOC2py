# _*_ coding: utf-8 _*_

import requests
from bs4 import BeautifulSoup 


value = {'content': 'r'}
url = "http://junjielizero.sinaapp.com/write"
r = requests.post(url, data=value)
soup = BeautifulSoup(r.text, "html.parser")
for i in soup.find_all('pre'):
  print i.get_text()


while True:
    content = raw_input("content: ")

    if content == '?':
        print '寻求帮助，请输入？'
        print '退出笔记，请按CTRL+C或请输入q'
        print '同步全部笔记历史，请按r'
        print '清除笔记，请输入delete'

    elif content == 'q':
      break

    else:
      value = {"content": content}  # 模拟网页手动输入，用字典方式传递
      url = "http://junjielizero.sinaapp.com/write"
      r = requests.post(url, data=value)
      soup = BeautifulSoup(r.text, "html.parser")
      for i in soup.find_all('pre'):
          print i.get_text()


