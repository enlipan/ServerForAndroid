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


def make_file_path(request_ulr):
    import urlparse
    urlparse.urlparse(request_ulr)
    open_path = os.path.join(os.path.abspath('.'), 'output' + urlparse.urlparse(request_ulr).path)
    if not os.path.exists(open_path):
        os.makedirs(open_path)
    return open_path + '/res_output.json'


def write_info_to_file(res_text, file_path):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    with open(file_path, 'w') as of:
        # unicode(info).encode('utf-8') 将unicode使用 utf-8编码处理中文字符
        print >> of, res_text.encode('utf-8')


def append_info_to_file(format_file_path, info):
    print format_file_path
    with open(format_file_path, 'a') as of:
        print info
        print >> of, info.encode('utf-8')


# 读取生成的接口JsonFile 生成对应格式的Info
# 订单中心 001 取消订单 /app/car/appcarsearchaction
def read_and_generate_format_file(file_path):
    format_file_path = os.path.join(os.path.dirname(file_path), 'format_output.json')
    if os.path.exists(file_path):
        with open(file_path) as json_data:
            jsonInfo = json.load(json_data)
            if len(jsonInfo['apis']) > 0:
                for index, jsonItem in enumerate(jsonInfo['apis']):
                    str_path = jsonItem['path']
                    print "str_path:------------------", str_path
                    append_info_to_file(format_file_path,
                                        str(index + 1) + '   ' + jsonItem['operations'][0]['summary'] + '   ' +
                                        jsonItem['description'] + '  ' + jsonItem['path'])


def fetch_domain_url(request_ulr):
    cookies = {'_security_token': '11bH5_lTwr91t2Bi',
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
    file_path = make_file_path(request_ulr)
    print file_path
    # write_info_to_file(response.text, file_path)
    # read_and_generate_format_file(file_path)


def fetch_with_session(request_url):
    pass


def fetch_with_ssl(request__https_url):
    res = requests.get(request__https_url, verify=True)
    pass


if __name__ == '__main__':
    print str(sys.argv)
    read_and_generate_format_file(
        '/Users/paul/Documents/Paul/PythonDemo/package/scrap/crapServer/output/api-docs/souche/app-car-info/res_output.json')
