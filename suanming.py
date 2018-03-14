#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import hashlib


def getorder(name, time, gender, model):
    name = name
    time = time
    url = 'https://sandbox.zxcs.linghit.com/api/v2/orders/register'
    data = {
        'username':'{}'.format(name),
        'birthday':'{}'.format(time),
        'pay_point':'{}'.format(model),
        'ma_id'	:'1dd23238-a33b-4bf8-f582-910e2187d410',
        'gender':gender
    }
    req = requests.post(url=url, data=data,verify=False)
    return (req.json()['order_id'])

def getsign(order_num):
    order_num = order_num
    money = '0.01'
    key = '64745fa3bd8c428ba7896efdc7286334'
    str = '{}{}{}'.format(order_num,money,key)
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return (hl.hexdigest())



def reqjson(orderid,sign):
    url = 'http://sandbox.zxcs.linghit.com/api/v1/pay/bxm/notify.json'
    data = {
        # 'orderId':orderid,
        'orderId': orderid,
        'money':'0.01',
        'sign':sign
        # 'sign': '31e76fa41a0affadf0c0d96206bb34bc'
    }
    req1 = requests.post(url=url,data=data)
    return (req1.json()['url'])


def run():
    modelist = ['mllyuncheng_default','bazijingpi_default',
                'ganqingyunshi_default','yishengcaiyun_default',
                'baziyunshi_default','zwzjingpi_default',
                'lianaitaohua_default']
    # 名称
    name = '王达康'
    # 生日
    time = '1998050610'
    # 性别   男 1 女 0
    gender = '0'
    # 模式  0-6
    model = modelist[6]

    orderid = getorder(name, time,gender, model)
    signnum = getsign(orderid)
    urlresult = reqjson(orderid,signnum)
    print(urlresult)

run()
