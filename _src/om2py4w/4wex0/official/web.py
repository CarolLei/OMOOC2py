import urllib
import urllib2

while True:
	content = raw_input("content: ")
    values = {"content": content}
    data = urllib.urlencode(values)
    url = "http://localhost:8090/write"
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    file = open('all.txt','r')
    print file.read()
    file.close()





