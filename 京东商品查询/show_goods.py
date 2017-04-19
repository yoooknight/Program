# encoding:utf-8
# author: WangSong
"""命令行查询京东商品
Usage:
    show_goods <url>

Options:
    -h,--help   显示帮助菜单

Example:
    show_goods https://item.jd.com/3133817.html
"""

from docopt import docopt       # 通过docopt来获取命令行参数
import re                       # 正则表达式抓取页面信息
from bs4 import BeautifulSoup   # 用re来匹配html比较繁琐，用这个比较方便快捷==!
import urllib.request
from prettytable import PrettyTable
import json

# 连接url并且访问返回页面信息
class url_connect:
    t_header = '商品 普通价格 会员价格 超级会员价格 好评率'.split()
    def __init__(self, url):
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
        self.url = url

    # 获取该链接的响应
    def getresponse(self, url):
        try :
            req = urllib.request.Request(url, headers=self.header)
            resp = urllib.request.urlopen(req, timeout=5)
            content = resp.read()
            # 将获取到的内容写入文件
            fh = open("jd.html", "wb")
            fh.write(content)
            fh.close()

            return content
        except ValueError:
            print("please input the right website：[ https://item.jd.com/3133817.html ]")
            return

    # 这里检测传入的链接是否是京东页面的商品链接，如果不是则报错
    def check_base_url(self):
        pattern_url = re.compile(r"^https://item.jd.com/\d+.html$")
        res = pattern_url.match(self.url)
        if res == None:
            exit("please input the right website：[ https://item.jd.com/3133817.html ]")

    # 获取到商品id
    def get_goods_id(self):
         # 获取到商品id
        pattern_id = re.compile(r"https://item.jd.com/(\d+).html")
        res=pattern_id.match(self.url)
        self.goods_id = res.group(1)
        return self.goods_id

        # 将检测url的工作单独独立出来,这里就不用检测了
        # if res != None:
        #     self.goods_id = res.group(1)
        #     return self.goods_id
        # else:
        #     print("please input the right website：[ https://item.jd.com/3133817.html ]")
        #     return

    # 获取商品名称
    def get_goods_name(self, content):
        # 正则有问题，不能懒惰匹配，这个以后再来想，直接换bs4来抓取
        # pattern_name = re.compile(r'<div class="sku-name">([\s\S]*)</?div>')
        # a = re.findall(pattern_name, content)

        # content = content.decode("utf-8", errors = "ignore")  # 不用转码了
        # 这里获取到的名字会有乱码，百度后，用gb18030编码就正确了，具体原因没有深究
        try:
            soup = BeautifulSoup(content, "html.parser", from_encoding="gb18030")
            ret = soup.find_all("div", {"class":"sku-name"})
            return ret[0].string.strip()
        except:
            return False


    # 获取商品价格
    def get_goods_price(self):
        try:
            goods_id = self.get_goods_id()
            price_url = "https://p.3.cn/prices/mgets?skuIds=J_" + goods_id
            return json.loads(self.getresponse(price_url).decode())
        except:
            return False

    # 获取商品好评率
    def get_goods_rate(self):
        try:
            goods_id = self.get_goods_id()
            rate_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + goods_id + "&callback=jQuery2931016"
            # 返回的格式是jQuery2931022(这里是需要的json数据)
            # GoodRateShow
            ret_rate = self.getresponse(rate_url).decode(errors="ignore")
            pattern_rate = re.compile('jQuery\d+\((.*)\);')
            ret_rate_json = pattern_rate.match(ret_rate)
            return json.loads(ret_rate_json.group(1))['CommentsCount'][0]['GoodRateShow']
        except:
            return False

    def pretty_print(self, name, p_price, m_price, op_price, comment_rate):
        try:
            # 处理价格位-1的数据
            p_price = (p_price if float(p_price)>0 else "未报价")
            m_price = (m_price if float(m_price)>0 else "未报价")
            op_price = (op_price if float(op_price)>0 else "未报价")

            pt = PrettyTable()
            pt._set_field_names(self.t_header)
            l = [name, p_price, m_price, op_price, comment_rate]
            pt.add_row(l)
            print(pt)
        except:
            exit("the param to print are wrong")

def show_goods():
    """command-line interface"""
    # 1. 接收参数
    arguments = docopt(__doc__)    
    url = arguments['<url>']
    # print(url)

    # 2. 链接页面，获取信息
    conn = url_connect(url)
    # 检测网页，如果出错则直接终端
    conn.check_base_url() 

    content = conn.getresponse(url)

    # 3. 获取商品名称
    name = conn.get_goods_name(content)
    # if name==False:        
    #     print("the goods did not exists")
    #     exit()
    if name == False:
        exit("the goods did not exists")

    # print(name)

    # 4. 居然没有价格，通过网络抓包，发现价格是通过这个url来获取的
    # https://p.3.cn/prices/mgets?callback=jQuery7419219&type=1&area=1&pdtk=&pduid=14925976302301747162816&pdpin=&pdbp=0&skuIds=J_3133817
    # 有些参数不知道怎么获取，我发现只要传递https://p.3.cn/prices/mgets?skuIds=J_3133817，商品号也是可以获取到这些信息的
    # 返回的格式是[{"id":"J_10450240174","p":"8.50","m":"42.00","op":"14`.90"}]
    price = conn.get_goods_price()[0]
    if price == False:
        exit("the price get wrong response")
    # print(price['p'])
    # print(price['m'])
    # print(price['op'])

    # 5. 获取好评率
    # 同理，好评率通过网址
    # https://club.jd.com/comment/productCommentSummaries.action?referenceIds=3133817&callback=jQuery2931016&_=1492597631236
    # 经测试，最后一个参数不明白是怎么获取，去掉之后没有影响结果
    # https://club.jd.com/comment/productCommentSummaries.action?referenceIds=3133817&callback=jQuery2931016
    comment_rate = conn.get_goods_rate()
    if comment_rate == False:
        exit("the rate get wrong response")
    # print(comment_rate)

    # 6. 用pretty展示出来
    conn.pretty_print(name, price['p'], price['m'], price['op'], comment_rate)


if __name__ == "__main__":
    show_goods()