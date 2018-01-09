# -*- coding:utf-8 -*-
# !/usr/bin/env python

from util.common import check_proxy_ip
import pymysql
import time


class MysqlSaver:
    cursor = None
    db = None
    save_sql = ""

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "DB_Proxy")
        self.save_sql = "INSERT INTO TB_Proxy_Info (`protocol`, `ip`, `port`, `add_time`, `source_ad`) VALUES('{protocol}', '{ip}', '{port}', '{add_time}', '{source_ad}')"
        self.get_sql = "SELECT * FROM TB_Proxy_Info"
        self.del_sql = "DELETE FROM TB_Proxy_Info WHERE `id` = '{id}'"
        self.cursor = self.db.cursor()

    def save_proxy(self, ip_list, source_ad):
        for ip_info in ip_list:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            sql = self.save_sql.format(protocol=ip_info['protocol'], ip=ip_info['ip'],
                                                    port=ip_info['port'], source_ad=source_ad, add_time=current_time)
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except Exception:
                print(Exception)
                self.db.rollback()

    def close(self):
        self.db.close()

    def get_proxy(self):
        try:
            self.cursor.execute(self.get_sql)
            result = self.cursor.fetchall()
            self.db.commit()
        except Exception:
            print("异常", Exception)
            self.db.rollback()

        return result
        

    def clear(self):
        all_proxies = self.get_proxy()        
        for proxy in all_proxies:
            res = check_proxy_ip(proxy[1].lower(), proxy[2], proxy[3])
            if res is False:
                sql = self.del_sql.format(id=proxy[0]) 
                try:
                    print(proxy[2] + "已失效")
                    self.cursor.execute(sql)
                    self.db.commit()
                except Exception:
                    print("delete failed")
                    self.db.rollback()

