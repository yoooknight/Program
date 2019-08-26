#coding=utf-8

from bs4 import BeautifulSoup
from urllib.request import quote
import urllib.request
import string
import re

class Spider:
    search = ''
    indexUrl = 'http://www.pinghaoche.com.cn/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

    def __init__(self, search):
        self.search = search

    def getlinkList(self):
        # 搜索文件
        searchUrl = self.indexUrl + '?s=' + self.search
        searchUrl = quote(searchUrl, safe=string.printable)

        req = urllib.request.Request(searchUrl, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf8')

        # with open('index.html', 'a', encoding='utf-8') as f:
        #     f.write(html)

        # 读取爬取下来的网页数据
        # with open('index.html', encoding='utf-8') as f:
            html = f.read()

        # 读取详情页面
        soup = BeautifulSoup(html, 'html.parser')
        detailUrl = soup.find('div', class_='mainleft').find('div', class_='thumbnail').find('a').get('href')

        # 获取详情页面
        detailReq = urllib.request.Request(detailUrl, headers=self.headers)
        detailRes = urllib.request.urlopen(detailReq)
        detailHtml = detailRes.read().decode('utf-8')

        # with open('detail.html', 'a', encoding='utf-8') as f:
        #     f.write(detailHtml)

        # with open('detail.html', encoding='utf-8') as f:
        #     detailHtml = f.read()

        # print(detailHtml)

        soup2 = BeautifulSoup(detailHtml, 'html.parser')
        b = soup2.find('div', id='link-report').select('h2>span')[0].get_text()

        c = b.split(": ")
        linkUrl = c[1].split(" ")[0]
        code = c[2].split(" ")[0]

        return {'link': linkUrl, 'code': code}
