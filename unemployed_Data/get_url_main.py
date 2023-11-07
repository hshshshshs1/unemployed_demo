# -*- coding: UTF-8 -*-
# @Time : 2023/10/18 8:51
# @Author : 重邮郝开心
# @File : main
# @Project : 爬虫
from unemployed_Data.auto_get_unemployed_data_url.baidu import *
from unemployed_Data.auto_get_unemployed_data_url.get_unemployed_url import *
from urllib.parse import quote


if __name__ == '__main__':
    keyword = input("请输入搜索的关键字：")
    page = int(input("请输入要搜索的页数："))
    for i in range(page):
        # 定制请求头
        request = get_request_1(quote(keyword), page)
        # 获取网页内容
        htmlcontent = get_content(request)
        # 获取带有数据地址的h3标签内容
        h3_list = get_h3(htmlcontent)
        # 获取url地址
        url_list = get_url(h3_list)
        # 将地址写到文件中
        with open(f'{keyword}.txt', 'a', encoding='utf-8') as f:
            for elem in url_list:
                f.write(elem)
                f.write('\n')

