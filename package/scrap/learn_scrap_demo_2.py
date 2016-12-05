# coding=utf-8
__author__ = 'Lee'

import re
from learn_scrap_demo_1 import download_retry

"""
sitemap 遍历
"""


def down_print_link(link):
    html = download_retry(link)
    print 'html --> %s \n' % html


def craw_sitemap(url):
    sitemap = download_retry(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    [down_print_link(link) for link in links]

# craw_sitemap('http://example.webscraping.com/sitemap.xml')
