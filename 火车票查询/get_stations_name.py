# encoding:utf-8

from docopt import docopt
import re
import requests
from pprint import pprint
from stations import stations
from prettytable import PrettyTable

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9002'

response = requests.get(url, verify=False)

stations = re.findall( u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
