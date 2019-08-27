# encoding=utf8
from sourceSpider.pinghaoche import spider as pingSpider
from sourceSpider.staticPage import spider as pageSpider

# reload(sys)
# sys.setdefaultencoding('utf8')

# a = pingSpider.Spider('致命女人')
a = pageSpider.Spider("致命女人")
b = a.getlinkList()
print(b)
