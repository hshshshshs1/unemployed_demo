# -*- coding: UTF-8 -*-
# @Time : 2023/10/18 8:53
# @Author : 重邮郝开心
# @File : baidu.com
# @Project : 爬虫

import urllib.request
from chardet import detect
import requests
import gzip


def get_request_1(keyword, page):
    """
    定制请求头
    :param keyword:
    :param page:
    :return:
    """
    page_start_num = (page-1) * 10
    url = 'https://www.baidu.com/s?wd=keyword&pn=' + str(page_start_num)
    url = url.replace('keyword', keyword)
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN, zh;q = 0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PSTM=1676374030; BAIDUID=733B4018C8E98AF7DB3993DE971E7517:FG=1; BIDUPSID=9CE3770DB54544DC6163434F84AF629A; MCITY=-132%3A; sugstore=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS_BFESS=lRDZH5tMktDanhKczVtMmo1T1lIUDZPc3BObFNmWDdaNX5CTlJvSDVpOFpBVk5sRUFBQUFBJCQAAAAAAAAAAAEAAADn-wZU7cK9o7T9t6IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABl0K2UZdCtlR; H_PS_PSSID=39327_39363_39415_39436_39528_39497_39234_26350_39428; ZFY=1VRCYWz6ZusX67Vt6m:BwIdT4Wo11:BbJkeomYxFMqqfA:C; BAIDUID_BFESS=733B4018C8E98AF7DB3993DE971E7517:FG=1; B64_BOT=1; delPer=0; BD_CK_SAM=1; PSINO=7; BA_HECTOR=8k24a1a40la4a481a4al2k0t1iiubld1o; H_PS_645EC=d932fwIxuFukWil1bPeSNRROP8ZTPaKBEBwTA8IeuPUSat81ZBgOWs8HDVo',
        'Host': 'www.baidu.com',
        'Sec-Ch-Ua': 'Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': "Windows",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.361'
    }
    # 定制请求头
    request = urllib.request.Request(url, headers=headers)
    result = []
    charset = get_encoding(url)
    result.append(request)
    result.append(charset)
    return result


def get_encoding(url):
    """
    获取网址的编码格式
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.encoding
        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常：", e)


def get_charset(url,i):
    """
    获取网页的charset
    :param url:
    :return:
    """
    print(i)
    print("\n")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type')
            charset = content_type.split('charset=')[-1]
            return charset
        else:
            print("请求失败，状态码：", response.status_code)
    except requests.exceptions.RequestException as e:
        print("请求异常：", e)


def get_request_2(url):
    """
    通过传入url定制请求头
    :param url:
    :return:
    """
    # 请求头
    headers = {
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN, zh;q = 0.9',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'Cookie': 'PSTM=1676374030; BAIDUID=733B4018C8E98AF7DB3993DE971E7517:FG=1; BIDUPSID=9CE3770DB54544DC6163434F84AF629A; MCITY=-132%3A; sugstore=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS_BFESS=lRDZH5tMktDanhKczVtMmo1T1lIUDZPc3BObFNmWDdaNX5CTlJvSDVpOFpBVk5sRUFBQUFBJCQAAAAAAAAAAAEAAADn-wZU7cK9o7T9t6IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABl0K2UZdCtlR; H_PS_PSSID=39327_39363_39415_39436_39528_39497_39234_26350_39428; ZFY=1VRCYWz6ZusX67Vt6m:BwIdT4Wo11:BbJkeomYxFMqqfA:C; BAIDUID_BFESS=733B4018C8E98AF7DB3993DE971E7517:FG=1; B64_BOT=1; delPer=0; BD_CK_SAM=1; PSINO=7; BA_HECTOR=8k24a1a40la4a481a4al2k0t1iiubld1o; H_PS_645EC=d932fwIxuFukWil1bPeSNRROP8ZTPaKBEBwTA8IeuPUSat81ZBgOWs8HDVo',
        # 'Host': 'www.baidu.com',
        # 'Sec-Ch-Ua': 'Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99',
        # 'Sec-Ch-Ua-Mobile': '?0',
        # 'Sec-Ch-Ua-Platform': "Windows",
        # 'Sec-Fetch-Dest': 'document',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-Site': 'none',
        # 'Sec-Fetch-User': '?1',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61'
    }
    charset = get_encoding(url)
    print(charset)
    # 定制请求头
    request = urllib.request.Request(url, headers=headers)
    return [request, charset]


def get_content(rq):
    """
    爬取网页的内容
    :param rq:
    :return:
    """
    response = urllib.request.urlopen(rq[0])
    # print(rq[1])
    # print(response.read())
    if rq[1] == 'utf-8':
        print(2)
        html_content = response.read().decode('utf-8', 'ignore')
        return html_content
    else:
        # print(3)
        # html_content = gzip.decompress(html_content).decode('gbk', 'ignore')
        html_content = response.read().decode('gbk', 'ignore')
        return html_content


if __name__ == '__main__':
    # request = get_request_1(quote('全球公司裁员情况'), 2)
    # get_request_1(quote('Global company layoffs'), 2)
    # print(get_content(request))
    # request_list = get_request_2('http://www.baidu.com/link?url=pU3ZqaCqSZvA4-aVitS6EPbK78-_GfmRiE5oSgBrQPpoTiKrM0xCFZc1fduH6v-pmVyr55v8hNCwB6S4RBK0Y_92fC5jWXGgz6_X-SPyGM3')
    # print(request_list[1])
    # get_request_2('http://www.baidu.com/link?url=r1mVQr2kVVAtvOW_wbS0TQhaw62-_X5OwdfcX7FJXQqGS-aP23rEjS3uvN-9i-iT')
    # print(get_content(request_list))
    # get_content(request_list)
    print(get_charset('http://www.baidu.com/link?url=3tNpUvMBzgujc_jusPJMm1PQaLR6LKyOU2aSCK5tcvePpADP0zN3HOGEn8NnsSP0sGCm4oLdHC2A6L0ZHRp3PjV9js--oVNCZQlf0baMv77',1))
    print(get_charset('http://www.baidu.com/link?url=awXKMh7VUBIyMCTLal7lk-mB40qDXmmHQ13tesBSdUeNbyG0owGOQ-Raf3zBrcJPY-Iv7oP4wdqaEbkhy_H_4a',2))


