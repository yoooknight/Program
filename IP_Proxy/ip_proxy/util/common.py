# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Program: some common functions
Author: YoooKnight
History: First Released 2017/12/25
"""

from http_mng.manage import o


def check_proxy_ip(ip_proxy):
    oi = o("http://2017.ip138.com/ic.asp", ip_proxy=ip_proxy)
    if oi.get_html_content() == "Error Connected":
        return False
    else:
        return True
