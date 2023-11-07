# -*- coding: UTF-8 -*-
# @Time : 2023/10/18 9:52
# @Author : 重邮郝开心
# @File : get_unemployed_url
# @Project : 爬虫
import re


def get_h3(content):
    """
    获取带有unemployed数据地址的h3
    :param content: 网页的代码内容
    :return:
    """
    s = r'<h3 class="c-title t t tts-title">[\s\S]*?(.*?)[\s\S]*?</h3>'
    re_com = re.compile(s)
    h3_list = []
    # print(type(h3_list))
    # print(len(h3_list))
    # print(re.finditer(re_com, content).group(0))
    for elem in re.finditer(re_com, content):
        if elem:
            h3_list.append(elem.group(0))
    return h3_list


def get_url(h3_list):
    """
    获取url地址，并返回
    :param h3_list: 带有unemployed数据地址的h3
    :return:
    """
    url_list = []
    for elem in h3_list:
        s = r'(http|https|ftp):\/\/[\w\-]+(\.[\w\-]+)*([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'
        re_com = re.compile(s)
        for e in re.finditer(s, elem):
            if e:
                url_list.append(e.group(0))
    return url_list
