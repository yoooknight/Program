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
        # 读取爬取下来的网页数据
        with open('index.html', encoding='utf-8') as f:
            html = f.read()

        # 读取详情页面
        with open('detail_7.html', encoding='utf-8') as f:
            detailHtml = f.read()

        dic = []

        soup = BeautifulSoup(detailHtml, 'html.parser')
        postContent = soup.find("div", id="post_content")
        # print(h2Content)

        # linkUrl = h2Content.find("a").get("href")

        # c = soup.find("div", id="link-report").find("h2")
        # print(c)

        aList = soup.findAll("a")
        # print(aList)
        # print(postContent)

        linkUrlList = []
        for aTag in aList:
            tempHref = aTag.get("href")

            if tempHref and tempHref.find("pan.baidu.com")>=0:
                linkUrlList.append(tempHref)

        # nn = re.search('提取码\: .{4}', str(postContent) + "提取码: mnxf")
        codeList = re.findall('((提取码|密码)[\:\：][ ]?.{4})', str(detailHtml))

        # print(type(str(postContent)))
        # print(nn)
        # print(str(postContent))
        # print(nn.group(1))

        # c = b.split(": ")
        # linkUrl = c[1].split(" ")[0]
        # code = c[2].split(" ")[0]
        # print(codeList)
        # print(linkUrlList)
        # print(aList)

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