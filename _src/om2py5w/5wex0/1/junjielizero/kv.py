# _*_ coding: utf-8 _*_
import sae.kvdb
import time
from pprint import pprint

date = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime())

kv = sae.kvdb.Client()
taglist = []

for i in xrange(12):
  k = 's#' + str(i)
  kv.set(k, i)

for k in sorted(kv.getkeys_by_prefix('s#'),key=lambda x:int(x.split('#')[-1])):
  taglist.append(kv.get(k))

print taglist









# 选择性tag，tag由之前的控制
'''
while True:

  tag = raw_input("> ")

  key = tag + ':'

  input = 0

  for i in xrange(11):
  	k = tag + ':' + str(i)
  	input = input + 1
  	kv.set(k, input)

  print sorted(kv.getkeys_by_prefix(key),key=lambda x:int(x.split(':')[-1]))

  for k in sorted(kv.getkeys_by_prefix(key),key=lambda x:int(x.split(':')[-1])):
    print kv.get(k)
'''
