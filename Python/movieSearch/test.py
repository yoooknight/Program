# encoding=utf8
from sourceSpider.pinghaoche import spider as pingSpider
from sourceSpider.staticPage import spider as pageSpider

# reload(sys)
# sys.setdefaultencoding('utf8')

a = pingSpider.Spider('怪奇物语')
# a = pageSpider.Spider("致命id")
b = a.getlinkList()
print(b)
