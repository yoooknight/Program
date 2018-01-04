# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Program: some common functions
Author: YoooKnight
History: First Released 2017/12/25
"""

from http_mng.manage import o
from bs4 import BeautifulSoup


def check_proxy_ip(ip_proxy):
    # oi = o("http://2017.ip138.com/ic.asp", False, ip_proxy)
    print(ip_proxy)
#    oi = o("http://2017.ip138.com/ic.asp", False, ip_proxy={"HTTP": "113.121.38.9:808811"})
    oi = o("http://2017.ip138.com/ic.asp", False, ip_proxy={"http":"113.121.38.79:808"})
    res = oi.get_html_content() 
    print(res)
    if res == "Error Connected":
        return False
    else:
        return True
