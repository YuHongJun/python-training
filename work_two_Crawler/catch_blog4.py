#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#爬取简书上某个文章地址的主体内容
__author__ = 'Demi Yu'

from bs4 import BeautifulSoup
import requests
import codecs


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def get_text(html):
    parser = BeautifulSoup(html, 'html.parser')
    article = parser.find('div', attrs={'class': 'article'})  # 定位文章
    title = article.find('h1', attrs={'class': 'title'}).get_text()  # 获取标题
    text = []  # 创建空列表存放文章
    for paragraph in article.find_all('p'):
        paragraph_content = paragraph.get_text()
        text.append(paragraph_content)  # 将文章一段一段的添加到列表中
    return title, text


def save_text(title, text):
    file_name = title + '.txt'
    with codecs.open(file_name, 'wb', encoding='utf-8') as open_file:
        try:
            for p in text:
                open_file.write('\t%s\r\n' % p)  # \t是tab制表符，\r\n是Carrige Return换行
        except Exception:
            print('发生了错误！')
        print('文章抓取完成！')
        return


if __name__ == '__main__':
    url = 'http://www.jianshu.com/p/293c3b71416e'
    html = get_page(url)
    title, text = get_text(html)
    save_text(title, text)
