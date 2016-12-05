# coding=utf-8

import urllib2

"""
* 爬取网站地图
* 遍历网页数据库ID
* 跟踪网页链接
"""


def download(url):
    print 'Downloading...', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
    return html


def download_retry(url, num_retries=2):
    print 'Downloading...', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


"""
设置用户代理
"""


def download_agent(url, user_agent='wswp', num_retries=2):
    print 'Downloading...', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
    html = None
    if num_retries > 0:
        if hasattr(e, 'code') and 500 <= e.code < 600:
            return download(url, num_retries - 1)
    return html



# print download("http://example.webscraping.com")
# download_retry('http://httpstat.us/500')
