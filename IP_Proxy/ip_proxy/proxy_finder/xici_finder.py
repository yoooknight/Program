# -*- coding:utf-8 -*-
# !/usr/bin/env python
# http://api.xicidaili.com/free2016.txt

from http_mng.manage import o
from proxy_finder.finder import *
from util.common import check_proxy_ip
from bs4 import BeautifulSoup


class XiciFinder(finder):
    ip_list = []
    oi = None
    html_content = ""

    def __init__(self):
        # 初始化变量
        self.oi = o("http://www.xicidaili.com/")
        self.html_content = self.oi.get_html_content()

    def get_proxies(self):
        bs_content = BeautifulSoup(self.html_content, "html.parser")
        ip_html = bs_content.select("#ip_list")[0]
        ip_list_tmp = ip_html.find_all("tr")
        del ip_list_tmp[0:3]

        for ip_info_tmp in ip_list_tmp:
            ip_info = ip_info_tmp.find_all("td")
            if ip_info:
                protocol = ip_info[5].contents[0]
                port = ip_info[2].contents[0]
                ip = ip_info[1].contents[0]
                res = check_proxy_ip({protocol: ip + ":" + port})
                res = True

                if res:
                    ip_tmp_dic = {
                        "ip": ip,
                        "port": port,
                        "protocol": protocol
                    }
                    self.ip_list.append(ip_tmp_dic)
        return self.ip_list


def test():
    """
     <tr class="">
    <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
    <td>121.31.199.91</td>
    <td>6675</td>
    <td>广西桂林</td>
    <td class="country">高匿</td>
    <td>socks4/5</td>
      <td>1138天</td>
    <td>大约 2 年</td>
    </tr>
    """
    ip_list_final = []
    oi = o("http://www.xicidaili.com/")
    
    res = oi.get_html_content()

    bs_res = BeautifulSoup(res, "html.parser")
    ip_html = bs_res.select("#ip_list")[0]
    ip_list = ip_html.find_all("tr")
    del ip_list[0:3]

    for ip_info_html in ip_list:
        ip_info = ip_info_html.find_all("td")
        if ip_info:
            ip_tmp_dic = {
                "ip": ip_info[1].contents[0],
                "port": ip_info[2].contents[0],
                "protocol": ip_info[4].contents[0]
            }
            ip_list_final.append(ip_tmp_dic)

    print(ip_list_final)
    # print(res