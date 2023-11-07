# -*- coding: UTF-8 -*-
# @Time : 2023/10/18 11:21
# @Author : 重邮郝开心
# @File : get_content
# @Project : 爬虫
from unemployed_Data.auto_get_unemployed_data_url.baidu import *
import re


#获取页面内容，返回一个content
def get_url_content(url):
    """
    通过url地址获取裁员信息
    :param url:
    :return:
    """
    request = get_request_2(url)
    html_content = get_content(request)
    # print(html_content)
    return html_content


def get_p_content(content):
    """
    获取p标配的文本信息
    :param content:
    :return:
    """
    s = r'<p[\s\S]*?(.*?)[\s\S]*?</p>'
    re_com = re.compile(s)
    p_content_list = []
    new_p_content_list = []
    # 获取网页代码中的p标签及里面的内容
    for elem in re.finditer(re_com, content):
        if elem:
            p_content_list.append(elem.group(0))
    # 获取p标签里面的内容，不包含标签
    for elem in p_content_list:
        # 正则表达式字符串
        str1 = r'<[\s\S]*?(.*?)[\s\S]*?>'
        str1 = re.compile(str1)
        for i in elem:
            if '\u4e00' <= i <= '\u9fff':
                continue
            else:
                break
        for e in re.finditer(str1, elem):
            if e:
                elem = elem.replace(e.group(0), '')
        for i in elem:
            print(i)
            if '\u4e00' <= i <= '\u9fff':
                continue
            else:
                break
        new_p_content_list.append(elem)
    return new_p_content_list


#
def read_url_get_data(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        for url in fp.readlines():
            # url.strip() 去除地址后面的换行符
            html_contnet = get_url_content(url.strip())
            print(get_p_content(html_contnet))


if __name__ == '__main__':
    # html_content = get_url_content('http://www.baidu.com/link?url=pU3ZqaCqSZvA4-aVitS6EPbK78-_GfmRiE5oSgBrQPpoTiKrM0xCFZc1fduH6v-pmVyr55v8hNCwB6S4RBK0Y_92fC5jWXGgz6_X-SPyGM3')
    # print(html_content)
    # print(get_p_content(html_content))
    # get_p_content(html_content)
    read_url_get_data('C:\\Users\\Administrator\\Desktop\\code\\爬虫\\unemployed_Data\\全球裁员情况.txt')
