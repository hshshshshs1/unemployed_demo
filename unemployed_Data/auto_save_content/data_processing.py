# -*- coding: UTF-8 -*-
# @Time : 2023/10/10 17:01
# @Author : 重邮郝开心
# @File : data_processing
# @Project : 爬虫

import json
import pandas as pds


# 读取数据
with open('unemployed_data.json', 'r', encoding='utf-8') as fp:
    data = fp.read()
# 将json数据转换成dict
data = json.loads(data)
# 获取数据的表头
# ['Company', '# Laid Off', '%', 'Location HQ', 'Industry', 'Date']
# 表头列表
# ['Company', '# Laid Off', '%', 'Date']
name_list = []
data_name = data['data']['table']['columns']
for element in data_name:
    if element['name'] == 'Location HQ' or element['name'] == 'Industry':
        continue
    name_list.append(element['name'])
# print(name_list)
# 数据列表
company_data = []
laid_off_data = []
percentage_data = []
date_data = []
# 具体数据获取
data_unemployed = data['data']['table']['rows']
for element in data_unemployed:
    element_data = list(element['cellValuesByColumnId'].values())
    if len(element_data) != 6:
        continue
    else:
        company_data.append(element_data[0])
        laid_off_data.append(element_data[3])
        percentage_data.append(element_data[4])
        date_data.append(element_data[5][:10])
data_dict = dict()
data_dict[name_list[0]] = company_data
data_dict[name_list[1]] = laid_off_data
data_dict[name_list[2]] = percentage_data
data_dict[name_list[3]] = date_data

# 创建DataFrame对象
fwrite = pds.DataFrame(data_dict)

# 将数据写入excel文件中
fwrite.to_excel('unemployed.xlsx')


