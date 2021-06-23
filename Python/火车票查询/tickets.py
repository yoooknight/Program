# encoding:utf-8
"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt
import re
import requests
from pprint import pprint
from stations import stations
from prettytable import PrettyTable

class TrainsCollection:
    header = '車次 車站 時間 歷時 一等 二等 軟臥 硬臥 硬座 無座'.split()

    def __init__(self, avaliable_trains,options):
        """查詢到的火車班次集合

        :param avaliable_trains:一個列表，包含可獲得的火車班次，每個火車班次就是一個字典
        :param options:查詢的選項，如高鐵，動車，etc...
    
        """
        self.avaliable_trains = avaliable_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小時') + '分'
       
        # if duration.startswitch('00'):
        #     return duration[4:]
        # if duration.startswitch('0'):
        #     return duration[1:]
        return duration

    def trains(self):
        for raw_train in self.avaliable_trains:
            raw_train = raw_train['queryLeftNewDTO']
            
            train_no = raw_train['station_train_code']

            initial = train_no[0].lower()

            if not self.options or initial in self.options:
                train = [
                    train_no,        
                    '\n'.join([raw_train['from_station_name'],
                              raw_train['to_station_name']]),
                    '\n'.join([raw_train['start_time'],
                               raw_train['arrive_time']]),
                    self._get_duration(raw_train),
                    raw_train['zy_num'],
                    raw_train['ze_num'],
                    raw_train['rw_num'],
                    raw_train['yw_num'],
                    raw_train['yz_num'],
                    raw_train['wz_num'],
                ]
                yield train
        
    def pretty_print(self):
        pt = PrettyTable()

        pt._set_field_names(self.header)

        for train in self.trains():
            pt.add_row(train)
        print(pt)
            
            
    
def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
   
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']


    # 2017-0407的最新接口
    # https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-04-07&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=SHH&purpose_codes=ADULT


    # 构建URL
    # url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date, from_station, to_station)
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, from_station, to_station)


    # 獲取參數
    options = ''.join([
        key for key,value in arguments.items() if value is True
        ])

    # 添加verifu=False不验证证书
    r = requests.get(url, verify=False)    
    avaliable_trains = r.json()['data']
    
    TrainsCollection(avaliable_trains, options).pretty_print()
    
if __name__ == '__main__':
    cli()
