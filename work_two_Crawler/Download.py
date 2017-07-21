#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#http://cuiqingcai.com/3256.html
#http://www.xicidaili.com/nt/ 代理IP地址
__author__ = 'Demi Yu'

#限制IP访问频率，超过频率就断开连接。（这种方法解决办法就是，降低爬虫的速度在每个请求前面加上time.sleep；或者不停的更换代理IP，这样就绕过反爬虫机制啦！）
#后台对访问进行统计，如果单个userAgent访问超过阈值，予以封锁。（效果出奇的棒！不过误伤也超级大，一般站点不会使用，不过我们也考虑进去
#上面讲过有的网站会限制相同的User-Agent的访问频率，那我们就给他随机来一个User-Agent，不停的更换代理IP好了！去百度一下User-Agent，我找到了下面这些：

import requests
import re
import random
import time
from bs4 import BeautifulSoup

class download():

    def __init__(self):

        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

        self.iplist = []  ##初始化一个list用来存放我们获取到的IP
        html = requests.get("http://www.xicidaili.com/nt/",headers=headers)  ##不解释咯
        # iplistn = re.findall(r'r/>(.*?)<b', html.text, re.S)  ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
        # for ip in iplistn:
        #     i = re.sub('\n', '', ip)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
        #     self.iplist.append(i.strip())  ##添加到我们上面初始化的list里面
        iplistn=BeautifulSoup(html.text, 'lxml').table.find_all('tr')
        for ipItem in iplistn:
            # i = re.sub('\n', '', ipItem)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
            ipHost=ipItem.contents[3].string
            ipPort = ipItem.contents[5].string

            # ipPort=ipItem.select('td:nth-of-type(3)').find('td').get_text()
            ipAll=ipHost+':'+ipPort
            self.iplist.append(ipAll.strip())
        # print(self.iplist[1:])  'IP地址:端口',




        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get(self, url, timeout, proxy=None, num_retries=6): ##给函数一个默认参数proxy为空
        UA = random.choice(self.user_agent_list) ##从self.user_agent_list中随机取出一个字符串
        headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）

        if proxy == None: ##当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            try:
                return requests.get(url, headers=headers, timeout=timeout)##这样服务器就会以为我们是真的浏览器了
            except:##如过上面的代码执行报错则执行下面的代码

                if num_retries > 0: ##num_retries是我们限定的重试次数
                    time.sleep(10) ##延迟十秒
                    print(u'获取网页出错，10S后将获取倒数第：', num_retries, u'次')
                    return self.get(url, timeout, num_retries-1)  ##调用自身 并将次数减1
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist[1:])).strip()) ##下面有解释哦
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy,) ##代理不为空的时候

        else: ##当代理不为空
            try:
                IP = ''.join(str(random.choice(self.iplist[1:])).strip()) ##将从self.iplist中获取的字符串处理成我们需要的格式（处理了些什么自己看哦，这是基础呢）
                proxy = {'http': IP} ##构造成一个代理
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout) ##使用代理获取response
            except:

                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist[1:])).strip())
                    proxy = {'http': IP}
                    print(u'正在更换代理，10S后将重新获取倒数第', num_retries, u'次')
                    print(u'当前代理是：', proxy)
                    return self.get(url, timeout, proxy, num_retries - 1)
                else:
                    print(u'代理也不好使了！取消代理')
                    return self.get(url, 3)

request = download()  ##


# if __name__ == '__main__':
#     request=download()
#     request.get('http://www.mzitu.com/all',3)
