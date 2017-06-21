# -*- coding: UTF-8 -*-
import os
import sys
import getopt
import requests
import json
import time

# python test.py  arg1 arg2
# Accept:application/json;charset=utf-8,*/*
# Accept-Encoding:gzip, deflate
# Accept-Language:zh-CN,zh;q=0.8,en;q=0.6
# Connection:keep-alive
# Cookie:sgsa_id=souche.com|1477308440052807; gr_user_id=325c2771-20de-439f-b60d-73948efcb5a4; channel=website; _qddaz=QD.1efojk.umx22h.iunzawha; matchtype=2; locat_cost=0; __utma=121281372.640024446.1498020259.1498020259.1498026097.2; __utmb=121281372.4.7.1498026107584; __utmc=121281372; __utmz=121281372.1498026097.2.2.utmcsr=devsso.sqaproxy.souche.com|utmccn=(referral)|utmcmd=referral|utmcct=/redirect.htm; _security_token=1Lors_lTwr91t2Bi
# DNT:1
# Host:erp-dev2.sqaproxy.souche.com
# Referer:http://erp-dev2.sqaproxy.souche.com/api
# TT:
# User-Agent:Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36
# X-Requested-With:XMLHttpRequest
# server_url = 'http://erp-dev2.sqaproxy.souche.com/api-docs/souche/app-car-info?_=1498029958834'
server_url = 'http://erp-dev2.sqaproxy.souche.com/api-docs'
server_url_info = server_url + '/souche/app-car-info'


# /souche/app-car-action
# + _:1498029958833 unix 时间戳



def fetch_domain_url(request_ulr):
    cookies = {'_security_token': '1Lors_lTwr91t2Bi',
               'sgsa_id': 'souche.com|1477308440052807',
               'gr_user_id': '325c2771-20de-439f-b60d-73948efcb5a4',
               'channel': 'website',
               '_qddaz': 'QD.1efojk.umx22h.iunzawha',
               'matchtype': '2',
               'locat_cost': '0',
               '__utma': '121281372.640024446.1498020259.1498020259.1498026097.2',
               '__utmb': '121281372.4.7.1498026107584',
               '__utmc': '121281372',
               '__utmz': '121281372.1498026097.2.2.utmcsr=devsso.sqaproxy.souche.com|utmccn=(referral)|utmcmd=referral|utmcct=/redirect.htm'
               }
    headers = {'Accept': 'application/json;charset=utf-8,*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest',
               'Host': 'erp-dev2.sqaproxy.souche.com',
               'Referer': 'http://erp-dev2.sqaproxy.souche.com/api'
               }
    params = {
        '_': time.time() * 1000
    }
    response = requests.get(request_ulr, params=params, headers=headers, cookies=cookies)
    from pprint import pprint
    pprint(response.headers)
    pprint(response.encoding)
    pprint(type(response.text))
    open_path = os.path.join(os.path.abspath('.'), 'output/output.json')
    reload(sys)
    sys.setdefaultencoding('utf-8')
    with open(open_path, 'w') as of:
        # unicode(info).encode('utf-8') 将unicode使用 utf-8编码处理中文字符
        print >> of, response.text.encode('utf-8')


def fetch_with_session(request_url):
    pass


def fetch_with_ssl(request__https_url):
    res = requests.get(request__https_url, verify=True)
    pass


if __name__ == '__main__':
    print str(sys.argv)
    fetch_domain_url(server_url_info)
