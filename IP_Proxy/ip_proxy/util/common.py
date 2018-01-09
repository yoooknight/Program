# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
Program: some common functions
Author: YoooKnight
History: First Released 2017/12/25
"""

from http_mng.manage import o
from bs4 import BeautifulSoup
import threading
import time


threadLock = threading.Lock()
threads = []
new_list = []


class myThread(threading.Thread):
    def __init__(self, protocol, ip, port):
        threading.Thread.__init__(self)
        self.protocol = protocol 
        self.ip = ip
        self.port = port
    def run(self):
        print "Starting" + self.name
        res = False
        # 获得锁，成功获得锁后返回True
        threadLock.acquire(5)
        res = check_proxy_ip(self.protocol, self.ip, self.port)
        # 释放锁
        threadLock.release()
        
        if res:
            new_list.append({"ip": self.ip, "protocol": self.protocol,  "port": self.port})

def check_proxy_ip(protocol, ip, port):
    ip_proxy = {protocol: ip + ":" + port}
    oi = o("http://2017.ip138.com/ic.asp", False, ip_proxy)
    res = oi.get_html_content() 
    print(res)
    if res == "Error Connected":
        return False
    else:
        return True

def check_proxy_list(proxy_list):
    thread_ins = []
    # 创建新线程
    for proxy_info in proxy_list:
        thread_ins.append(myThread(proxy_info['protocol'], proxy_info['ip'], proxy_info['port']))
        

    for i in thread_ins:
        i.start()

    for i in thread_ins:
        threads.append(i)

    # 开启新线程
    
    for t in threads:
        t.join(5)

    print"Exiting Main Thread" 
    return new_list
