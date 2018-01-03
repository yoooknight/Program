#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author: YoooKnight
History: First Released 2017/12/25
Program: manage the http request
"""

import urllib2


class o:
    __receive_html = ""        # 网页内容
    __receive_header = ""        # 返回的包头信息

    response = None
    test_url = "http://httpbin.org/ip"
    # 发送的请求头
    __send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    def __init__(self, url, headers=False, ip_proxy = False):
        if ip_proxy:
            proxy_handler = urllib2.ProxyHandler(ip_proxy)
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
      
        self.__send_headers = headers if headers else self.__send_headers
        
        try:
            req = urllib2.Request(url, headers=self.__send_headers)
            self.response = urllib2.urlopen(req)
        except Exception:
            pass

    def get_html_content(self):
        if self.response is not None:
            self.__receive_html = self.response.read()        #返回网页内容
            return self.__receive_html
        else: 
            return "Error Connected"

    def get_receive_header(self):
        if self.response is not None:
            self.__receive_header = self.response.info()        #返回网页内容
            return self.__receive_header
        else: 
            return "Error Connected"

if __name__ == "__main__":
    # o = o("http://www.baidu.com")
    # o = o("http://httpbin.org/ip", ip_proxy={"https":"115.29.163.82:808"})
    # o = o("http://2017.ip138.com/ic.asp", ip_proxy={"http":"115.29.163.82:808"})
    o = o("http://httpbin.org/ip")
    print(o.get_html_content())
    print(o.get_receive_header())
