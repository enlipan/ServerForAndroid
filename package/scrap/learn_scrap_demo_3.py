# coding=utf-8

__author__ = 'Lee'

import itertools
from learn_scrap_demo_1 import download_retry

""""
ID 遍历

猜测ID可用性，构建利用网页ID抓取网页数据
"""

max_errors = 5
num_error = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download_retry(url)
    if html is None:
        num_error += 1
        if num_error >= max_errors:
            break
    else:
        # 处理抓取的网页数据
        num_error = 0
        pass


