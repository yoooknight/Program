# -*- coding:utf-8 -*-
# !/usr/bin/env python

import pymysql
import time


class MysqlSaver:
    cursor = None
    db = None
    save_sql = ""

    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "DB_Proxy")
        self.save_sql = "INSERT INTO TB_Proxy_Info (`protocol`, `ip`, `port`, `add_time`, `source_ad`) VALUES('{protocol}', '{ip}', '{port}', '{add_time}', '{source_ad}')"
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

        self.close()

    def close(self):
        self.db.close()
