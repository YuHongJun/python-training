# from html.parser import HTMLParser
# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org/events/python-events/')
# class PythonEvent(HTMLParser):
#     def __init__(self):
#         super(PythonEvent, self).__init__()
#         self.key = 0
#         self.location_key = 0
#         self.event_list = []
#         self.event_tmp = []
#     def handle_starttag(self, tag, attrs):
#         if attrs:
#             if attrs[0][1] == 'event-title' or tag == 'time':
#                 self.key = 1 # self.key=1表示data需要保存
#             if attrs[0][1] == 'event-location':
#                 self.key = 1
#                 self.location_key =1 # self.location_key=1表示单个data信息结尾
#
#     def handle_data(self, data):
#         if self.key:
#             self.event_tmp.append(data)
#         if self.location_key:
#             self.event_list.append(self.event_tmp) # event_tmp保存进list并重置
#             self.event_tmp = []
#
#     def handle_endtag(self, tag):
#         self.key = 0
#         self.location_key = 0
#
# event = PythonEvent()
# event.feed(response.read().decode('utf-8'))
# for i in event.event_list:
#     print(i)

#from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k,v))
#     print('Data:', data.decode('utf-8'))

# from urllib import request
#
# req=request.Request('http://www.douban.com/')
# req.add_header('User-Agent','Mozilla/6.0 (iphone; CPU iphone os 8_0 like Mac OS X) AppleWebkit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s' %(k,v))
#     print('Data:', f.read().decode('utf-8'))

from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))