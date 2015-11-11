# _*_ coding: utf-8 _*_
# client1
import urllib
import urllib2


history = open('all.txt')
print history.read()
history.close()


while True:
    content = raw_input("content: ")

    if content == '?':
        print '打印当前，帮助输入？'
        print '退出笔记，请按CTRL+C'
        print '同步全部笔记历史，请按r'

    elif content == 'r':
      now = open('all.txt')
      print now.read()
      now.close()

    else:
      values = {"content": content}
      data = urllib.urlencode(values)
      url = "http://localhost:8090/write"
      request = urllib2.Request(url, data)
      response = urllib2.urlopen(request)
      file = open('all.txt','r')
      print file.read()
      file.close()
