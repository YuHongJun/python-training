# from PIL import Image
# im = Image.open('test1.jpg')
# print(im.format, im.size, im.mode)
# im.thumbnail((540,405))
# im.save('test44.bmp','BMP')

# import struct
#
# def judge(url):
#     with open(url,'rb') as f:
#         s=(f.read(30))
#         t=(struct.unpack('<ccIIIIIIHH',s))
#         if t[0]==b'B' and t[1]==b'M':
#             print('size:%s*%s\n color:%s'%(t[6],t[7],t[-1]))
#         else:
#             print(t)
#             print('size:%s*%s\n color:%s'%(t[6],t[7],t[-1]))
#
#
# url=input('Please enter the file address:')
#
# judge(url)

# import hashlib
#
# class Test(object):
# # db=test:win
#     db = {
#         'test': 'c967e1266b519854833aabceb116de07'
#     }
#     def get_md5(self,psw):
#         md5=hashlib.md5()
#         md5.update(psw.encode('utf-8'))
#         psw=md5.hexdigest()
#         return psw
#
#     def register(self):
#         username=input('Register: Please enter ur username:')
#         if username in self.db:
#             print('Username has existed')
#             exit()
#         else:
#             password=input('Register: Please enter ur password:')
#             self.db[username]=Test().get_md5(username+password+'the-Salt')
#
#     def login(self):
#         login_user=input('Login: Please enter your username:')
#         login_psw=input('Login: Please enter your password:')
#         login_psw=Test().get_md5(login_user+login_psw+'the-Salt')
#
#         passwd = self.db.get(login_user, -1)
#         if passwd==-1:
#             print('Username Error.')
#         elif self.db[login_user]!=login_psw:
#             print('Password Error.')
#         else:
#             print('Login Success.')
#
# t=Test()
# t.register()
# t.login()
import urllib.request, urllib.parse
from xml.parsers.expat import ParserCreate
class weatherSaxHandler(object):
    def __init__(self):
        self.location = {}
        self.forcast = []
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.location = attrs
        if name == 'yweather:forecast':
            self.forcast.append(attrs)
    def end_element(self, name):
        pass
    def char_data(self,text):
        pass

def parse_weather(xml):
    parser = ParserCreate()
    handler = weatherSaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    today = {
        'text': handler.forcast[0]['text'],
        'low': int(handler.forcast[0]['low']),
        'high': int(handler.forcast[0]['high'])
    }
    tomorrow = {
        'text': handler.forcast[1]['text'],
        'low': int(handler.forcast[1]['low']),
        'high': int(handler.forcast[1]['high'])
    }
    d = {
        'today': today,
        'tomorrow': tomorrow

    }
    d.update(handler.location)
    return d


# 测试:xml
# data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
# <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#         <title>Yahoo! Weather - Beijing, CN</title>
#         <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#         <yweather:location city="Beijing" region="" country="China"/>
#         <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#         <yweather:wind chill="28" direction="180" speed="14.48" />
#         <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#         <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#         <item>
#             <geo:lat>39.91</geo:lat>
#             <geo:long>116.39</geo:long>
#             <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#             <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#             <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#             <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#             <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#             <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#             <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#         </item>
#     </channel>
# </rss>
# '''


# weather = parse_weather(data)

# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# print('Weather:', str(weather))

def get_weather(city): # 输入城市名（拼音）字符串，输出天气dict
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % city
    yql_url = baseurl + urllib.parse.urlencode({'q':yql_query})
    print(yql_url)
    with urllib.request.urlopen(yql_url) as f:
        city_xml = f.read().decode('utf-8')
    city_weather = parse_weather(city_xml)
    return city_weather

def main():
    city = input('Weather Forecast in City: ')
    print(get_weather(city))

main()