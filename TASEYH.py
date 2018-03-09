# -*- coding: utf-8 -*-

import requests
from mysql import sqltest

proxies = {
  "http": "http://123.161.237.221:31215",
}
data = {'activityid': '12469',
        'appkey':'32bb6e97ac7e44328643fccab4f4h7287',
        'uid':'0D4E7071A1E4C65E5316B0ED6C863h54188A',
        'business':'money-1',}
req = requests.post('https://buy.bianxianmao.com/award/awardInfo',data=data, verify=False)
a = req.json()
print(a)
print(a['data']['awardid'])

b = a['data']['awardid']
sqltest(b)