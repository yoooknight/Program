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

        # 读取详情页面
        soup = BeautifulSoup(html, 'html.parser')
        try:
            # 这里只找了第一个链接，所有相当于是查找到相似度最高的一个结果
            detailUrl = soup.find('div', class_='mainleft').find('div', class_='thumbnail').find('a').get('href')

            # 获取详情页面
            detailReq = urllib.request.Request(detailUrl, headers=self.headers)
            detailRes = urllib.request.urlopen(detailReq)
            detailHtml = detailRes.read().decode('utf-8')

            dic = []

            # 查找所有的a标签
            soup = BeautifulSoup(detailHtml, 'html.parser')
            aList = soup.findAll("a")
            linkUrlList = []
            for aTag in aList:
                tempHref = aTag.get("href")

                if tempHref and tempHref.find("pan.baidu.com")>=0:
                    linkUrlList.append(tempHref)

            # 获取所有的提取码
            codeList = re.findall('((提取码|密码)[\:\：][ ]?.{4})', str(detailHtml))
            index=0
            for link in linkUrlList:
                if (index<len(codeList)):
                    tempDic = {
                        "link": link,
                        "code": codeList[index][0][-4:]
                    }
                    dic.append(tempDic)
                    index += 1

            return dic
        except Exception as e:
            print(e)
            return []
