# -*- coding:utf-8 -*- 
# /usr/bin/env python  

# # # # # # # # # # # # # # # # # # # # # # # # #
# Programe: ip_proxy.py                         #
#                                               #
# Author  : YoooKnight                          #
#                                               #
# History : First Released 2017/12/20           #
# # # # # # # # # # # # # # # # # # # # # # # # #

# from abc import ABCMeta, abstractmethod
# import ABC


class http_ins():
    


class IProxyFinder():
    ''' 
    查找免费代理IP的基类
    ''' 

    def find(self):
        pass


class IProxyFinder_xici(IProxyFinder):
    '''
    西刺免费代理
    '''
    def find(self):
        pass
    

class proxy_pool():
    '''
    代理池的管理：
    1. 获取可用代理IP
    2. 更新代理池IP    
    3. 保存代理池IP
    '''
    def init(self, finder, saver):
        self.finder = finder
        self.saver = saver

    def getOne(self):
        pass

    def refresh(self):
        pass
 
    def delete(self):
        pass



class IProxySaver():
    '''
    保存IP代理
    '''
    def save(ip_list):
        pass
 

if __name__ == "__main__":
    a = IProxyFinder()
    b = IProxySaver()
    a.find()
