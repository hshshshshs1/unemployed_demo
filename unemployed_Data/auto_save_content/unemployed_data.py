# -*- coding: UTF-8 -*-
# @Time : 2023/10/10 10:19
# @Author : 重邮郝开心
# @File : unemployed_data
# @Project : 爬虫

import urllib.request
from io import BytesIO
import gzip
import json


url = 'https://finance.eastmoney.com/a/202310062862639175.html'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie': 'qgqp_b_id=23d2669c0ad300ab04e81a33fa32591f; websitepoptg_api_time=1697344085086; st_si=64187238640889; websitepoptg_show_time=1697344085215; st_asi=delete; st_pvi=30813058790279; st_sp=2023-10-15%2012%3A28%3A05; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2F; st_sn=5; st_psi=20231015123523596-113104312931-3890248517',
    'Host': 'finance.eastmoney.com',
    'Referer': 'https://www.baidu.com/',
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',

}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read()
# content是gzip压缩过的数据，需要解压
buff = BytesIO(content)
f = gzip.GzipFile(fileobj=buff)
# 此时数据是字符串类型
content = f.read().decode('utf-8')
# # 使用json将数据转换成python对象
# data = json.loads(content)
# print(type(data))
with open('demo.txt', 'w', encoding='utf-8') as f:
    f.write(content)
