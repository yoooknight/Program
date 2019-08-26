# encoding=utf8
from sourceSpider.pinghaoche import spider as pingSpider

# reload(sys)
# sys.setdefaultencoding('utf8')

a = pingSpider.Spider('杀人回忆')
b = a.getlinkList()
print(b)