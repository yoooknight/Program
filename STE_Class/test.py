# -*- coding:utf-8 -*-
# /bin/env python
# author: YoooKnight
# History: First Released 抢课脚本模型完成，基于这个脚本可以重新进行修改完善


import json
import cookielib
import urllib2
from urllib import urlencode
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 登录成功后的链接
# "http://wechat.exc360.com/ukeywechat/student/index?token="
login_url = "http://wechat.exc360.com/ukeywechat/student/login"
sign_url = "http://wechat.exc360.com/ukeywechat/student/sign"
index_url = "http://wechat.exc360.com/ukeywechat/student/index?token="
token = ""


def login():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Content-Type': 'application/json',
    }
    filename = "cookie.txt"

    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    # tmp_cookie = urllib2.MozillaCookieJar(cookie)
    handler = urllib2.HTTPCookieProcessor(tmp_cookie)
    opener = urllib2.build_opener(handler)

    # print(zip(headers.keys(), headers.values()))
    opener.addheaders = zip(headers.keys(), headers.values())
    urllib2.install_opener(opener)

    # req = urllib2.Request(login_url, headers=headers)
    response = urllib2.urlopen(login_url)

    # print(response.headers)

    # if tmp_cookie:
        # print(tmp_cookie)

def sign():
    sign_url = "http://wechat.exc360.com/ukeywechat/student/sign"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Content-Type': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie':'SESSIONID=8269064EEA3B1B29675D427003E6DE21',
        'Referer': 'http://wechat.exc360.com/ukeywechat/student/login'
    }
    filename = "cookie.txt"

    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))

    data = urlencode({"username": "", "password": ""})

    req = urllib2.Request(sign_url, data=data, headers=headers)
    response = opener.open(req)

    # if tmp_cookie:
        # print(tmp_cookie)

    token = json.loads(response.read())['token']
    return token
    # print(token)


def chooseClass(token):
    #http://wechat.exc360.com/ukeywechat/student/bespoke/jplist
    #{  “token”:"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBwLnN0anAzNjAuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTUwOTU5OTQxNSwiZXhwIjoxNTEwODA5MDE1LCJuYmYiOjE1MDk1OTk0MTUsImp0aSI6InFJbmxjTEhBRGxIZEhET1ciLCJzdWIiOjM2NzQxfQ.yXbjcObPdE1p1wYyjTVGSo5VmNRHm8xw-JFXAN1ZkaE'",
    #    "date":"2017-11-5",
    #    "km":"",
    #    "startime":"2017-11-5 06:00",
    #    "endtime":"2017-11-5 21:00"
    #}

    no_student_list = []
    class_url = "http://wechat.exc360.com/ukeywechat/student/bespoke/jplist"
    filename = "cookie.txt"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Content-Type': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie':'SESSIONID=8269064EEA3B1B29675D427003E6DE21',
        'Referer': index_url + token
    }

    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))

    data = {
        "token": token,
        "date": "2017-11-24",
        "km": "",
        "startime": "2017-11-24%2006:00:00",
        "endtime": "2017-11-24%2021:00:00"
    }

    req = urllib2.Request(class_url, data=urlencode(data), headers=headers)
    response = opener.open(req)
    response_html = response.read()

    # 解析该文本，获取所选教练的所有空课程，解析出pid，
    # pid,日期，练车时间，教练
    bs = BeautifulSoup(response_html, "html5lib")
    class_list = bs.findAll("li", {'name': 'bespoke', 'coachname': '顾春雷C1'})
    # print(class_list)

    for class_info in class_list:
        # tmp_info = {}
        with open("john.txt", "a") as f:
            f.write(class_info.attrs['id'] + "  " +class_info.attrs['datestr'].decode('utf-8') + "  " + class_info.attrs['coachname'].decode('utf-8') + "  " + class_info.attrs['date'])

        class_type = class_info.findAll('h2')[0].contents[0]

        with open("john.txt", "a") as f:
            f.write("  " + class_type)

        # 查询该课程是否已经被选
        img_src = class_info.find('img')
        if img_src.attrs['src'] == "/ukeywechat/resource/student/images/pople_d.png":
            with open("john.txt", "a") as f:
                f.write("  " + "no student" + "\n")

            no_student_list.append(class_info.attrs['id'])
        else:
            with open("john.txt", "a") as f:
                f.write("  " + "has student" + "\n")

    print(len(class_list))
    print(no_student_list)
    return no_student_list

def finalClass(token, id_list):
    # /ukeywechat/student/bespoke/ok
    # {
    # "token":""
    # "pid":""
    # "spick_up":0 //（是否接送，默认是0）
    # }
    confirm_url = "http://wechat.exc360.com/ukeywechat/student/bespoke/ok"
    filename = "cookie.txt"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Content-Type': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie':'SESSIONID=8269064EEA3B1B29675D427003E6DE21',
        'Referer': index_url + token
    }
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))

    data = {
        "token": token,
        "pid": id_list[6],
        "spick_up": 0
    }

    req = urllib2.Request(confirm_url, data=urlencode(data), headers=headers)
    response = opener.open(req)
    response_html = response.read()
    print(response_html)

if __name__ == "__main__":
    login()
    token = sign()
    id_list = chooseClass(token)
    finalClass(token, id_list)
