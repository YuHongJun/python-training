#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Demi Yu'


# 基于py3.6 + pycharm
# 原地址：http://cuiqingcai.com/968.html
#
#
# 1.从服务器获取cookie，保存到变量中。
# 整体思路是：
# 先从cookiejar类中声明一个变量用来保存cookie→然后创建cookie处理器，用来处理cookie→创建打开器，读取处理好的cookie→创建请求，来生成cookie→ 将cookie读取到内存

# import http.cookiejar
# import urllib.request
#
# cookie = http.cookiejar.CookieJar()
# #声明一个CookieJar对象实例来保存cookie
# handler=urllib.request.HTTPCookieProcessor(cookie)
# #创建一个cookie的处理器，handler本质上是HTTPCookieProcessor类下的实例
# opener = urllib.request.build_opener(handler)
# #创建一个打开器opener，读取handler处理好的内容
# response = opener.open('http://www.baidu.com')
# #创建请求，来生成cookie。此处的open方法同urlopen方法，也可以传入request
# for item in cookie:
#     print ('Name = '+item.name)
#     print ('Value = '+item.value)
#



# 2.将cookie保存到文件。
# 整体思路是：
# 创建保存cookie工具的实例（同时指定文件名）→然后创建cookie处理器，用来处理cookie→创建打开器，用来读取处理好的cookie→创建请求，来生成cookie→将cookie保存到文件

# import http.cookiejar
# import urllib.request
#
# cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
# #创建保存cookie工具的实例（同时指定文件名）
# handler = urllib.request.HTTPCookieProcessor(cookie)
# #创建cookie处理器，用来处理cookie。handler本质上是HTTPCookieProcessor类下的实例
# opener = urllib.request.build_opener(handler)
# #创建打开器，用来读取处理好的cookie
# response = opener.open("http://www.baidu.com")
# #创建请求，来生成cookie
# cookie.save(ignore_discard=True, ignore_expires=True)
# #将cookie保存到文件
#


# 3.从文件中读取cookie并使用
# 整体思路：
# 创建空的cookie实例→从文件中读取cookie到变量→创建request请求→创建cookie处理器，用来处理cookie→创建打开器，用来读取已保存的cookie变量→发送请求，获得服务器的response→打印response


import http.cookiejar
import urllib.request

cookie = http.cookiejar.MozillaCookieJar()
#创建空的cookie实例
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#从文件中读取cookie到变量
req = urllib.request.Request("http://www.baidu.com")
#创建request请求
handler = urllib.request.HTTPCookieProcessor(cookie)
#创建cookie处理器，用来处理cookie
opener = urllib.request.build_opener(handler)
#创建打开器，用来读取已保存的cookie变量
response = opener.open(req)
#发送请求，获得服务器的response
print (response.read())
#打印response