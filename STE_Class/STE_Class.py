# -*- coding:utf-8 -*-
# /bin/env python
# author: YoooKnight
# History: 2017-11-23 第一次正式进行修改抢课脚本


import json
import cookielib
import urllib2
from urllib import urlencode
from bs4 import BeautifulSoup
import time
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 登录成功后的链接
# "http://wechat.exc360.com/ukeywechat/student/index?token="
login_url = "http://wechat.exc360.com/ukeywechat/student/login"
# sign_url = "http://wechat.exc360.com/ukeywechat/student/sign"
index_url = "http://wechat.exc360.com/ukeywechat/student/index?token="


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

    # 发送请求
    urllib2.urlopen(login_url)


def sign():
    sign_url = "http://wechat.exc360.com/ukeywechat/student/sign"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://wechat.exc360.com/ukeywechat/student/login'
    }
    filename = "cookie.txt"
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))

    data = urlencode({"username": "", "password": ""})
    req = urllib2.Request(sign_url, data=data, headers=headers)
    response = opener.open(req)

    token = json.loads(response.read())['token']
    return token


def chooseClass(token):
    no_student_list = []
    class_url = "http://wechat.exc360.com/ukeywechat/student/bespoke/jplist"
    filename = "cookie.txt"
    os.remove('john.txt')
    f_handle = open("john.txt", "a")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': index_url + token
    }

    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))
    data = {
        "token": token,
        "date": "2017-11-26",
        "km": "",
        "startime": "2017-11-26%2006:00:00",
        "endtime": "2017-11-26%2021:00:00"
    }
    req = urllib2.Request(class_url, data=urlencode(data), headers=headers)
    response = opener.open(req)
    response_html = response.read()

    # 解析该文本，获取所选教练的所有空课程，解析出pid，
    # pid,日期，练车时间，教练
    bs = BeautifulSoup(response_html, "html5lib")
    # class_list = bs.findAll("li", {'name': 'bespoke', 'coachname': '顾春雷C1'})
    class_list = bs.findAll("li", {'name': 'bespoke', 'coachname': '顾春雷C1'})
    if len(class_list) == 0:
        log("课程还没有发布，请稍后再试！")
        exit()

    for class_info in class_list:
        tmp_class_info = {}
        class_type = class_info.findAll('h2')[0].contents[0]
        class_id = class_info.attrs['id']
        class_datestr = class_info.attrs['datestr'].decode('utf-8')
        class_date = class_info.attrs['date']
        class_coachname = class_info.attrs['coachname'].decode('utf-8')

        f_handle.write(class_id + "  " + class_datestr + "  " + class_coachname + "  " + class_date + class_type)

        # 查询该课程是否已经被选
        img_src = class_info.find('img')
        if img_src.attrs['src'] == "/ukeywechat/resource/student/images/pople_d.png":
            f_handle.write("  " + "no student" + "\n")
            tmp_class_info['id'] = class_id
            tmp_class_info['datetime'] = class_type
            no_student_list.append(tmp_class_info)
        else:
            f_handle.write("  " + "has student" + "\n")

    print(no_student_list)
    return [no_student_list[2], no_student_list[3]]


def finalClass(token, id_list):
    confirm_url = "http://wechat.exc360.com/ukeywechat/student/bespoke/ok"
    filename = "cookie.txt"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': index_url + token
    }
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    tmp_cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(tmp_cookie))

    for pinfo in id_list:
        data = {
            "token": token,
            "pid": pinfo['id'],
            "spick_up": 0
        }
        req = urllib2.Request(confirm_url, data=urlencode(data), headers=headers)
        response = opener.open(req)
        response_html = response.read()

        status = json.loads(response_html)['status']
        if status == '406':
            log("当前的预约次数已经超过了本日限制")
            exit()
        else:
            log("课程" + pinfo['datetime'] + "选择成功!")


def log(info):
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    fhandle = open("result.log", "a")
    fhandle.write("[ " + current_time + " ]" + info + "\n")

if __name__ == "__main__":
    login()
    token = sign()
    id_list = chooseClass(token)
    finalClass(token, id_list)
