# -*- coding:utf-8 -*-
# !/usr/bin/env python


"""
Author:YoooKnight
Programe: Test...
History: Frist Released 2017/12/25
"""

from util.common import check_proxy_ip
from proxy_finder.xici_finder import XiciFinder
from proxy_saver.mysql_saver import MysqlSaver

if __name__ == "__main__":
    # pass
    a = XiciFinder()
    res = a.get_proxies()
    # print(res)
    # b = MysqlSaver()
    # b.save_proxy(res, "xici")
    # b.clear()
    # print(b.get_proxy())


    # print(res)
    # xici_finder.test()
    # proxy_ip = {'http':'110.72.37.239:8123'}
    # print(type(proxy_ip))

    # print check_proxyip(proxy_ip)

