import io
import json
from pprint import pprint

from package.server import *
from package.server.server_json import  getNetworkIp

"""
__init__.py  组织package内部 Module

from package.server import *  * 由该子包中的 __init__.py限定

from package.server.server_json import  getNetworkIp 非同一包结构引用情况

"""

try:
    with open('../file/content_file.json', 'r') as open_file:
        file_content = open_file.read()
        print file_content
        json_str = json.dumps(file_content)
        json_str = json.loads(json_str)
        pprint(json_str)
except IOError:
    print "file is not exist"
else:
    print "open file success"


