# -*- coding:utf-8 -*-
import urllib2, re, argparse, json, time
import pymysql as mdb
import utils, traceback, Queue, socket

class BaiduPanSpider(object):
    def __init__(self):
        self.db = Db()
        self.files = []
        self.got_files_count = 0
        self.got_follow_count = 0
        self.white_count = 0
        self.spider_queue = Queue.Queue(maxsize=20)
        self.status = 'stop'
        self.errno = ERR_NO
        self.file_type_t = {'video':0, 'image':1, 'document':2, 'music':3, 'package':4, 'software':5, 'torrent':6, 'other':7}

    def seedUsers(self):
        pass

    def startSpider(self):
        pass

# 程序主代码
if __name__ == '__main__':
    # 1. 收集参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed-user', help='get seed user', action='store_true')
    args = parser.parse_args()
    
    # 2. 爬虫实例
    spider = BaiduPanSpider()
    
    # 3. 做种?什么意思
    if args.seed_user:
        spider.seedUsers()
    else:
        while (1):
            print "start spider..."
            # 开始爬取数据
            result = spider.startSpider()
            if not result:
                print 'The spider is refused, 5mins later try again auto...'
                time.sleep(60 * 5)
            else:
                print 'one workder queue id done'
                time.sleep(1)
