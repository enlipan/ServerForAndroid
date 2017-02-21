# coding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
import json
import io
import os
import re

PORT_NUMBER = 8989
API_REGULAR = '/app/assess/assessaction/getCarRemindListV3.json'
FILE_NAME = 'content_order_leasing.json'


class JsonHandler(BaseHTTPRequestHandler):
    MESSAGE = ""
    """Json Handler"""
    def do_GET(self):
        # 对应的restApi
        if None != re.search(API_REGULAR, self.path):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            if self.MESSAGE == "":
                self.MESSAGE = getJsonStr()
            self.wfile.write(self.MESSAGE)
            return
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()


def getIPAddress():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("baidu.com", 80))
    s_name = s.getsockname()[0]
    s.close()
    return s_name


def getJsonStr():
    try:
        with open(os.path.join(os.path.dirname(__file__) + '/../file/' + FILE_NAME), 'r') as open_file:
            message = open_file.read()
            # json.dumps()
            # json.loads()
            return message
    except IOError:
        pass


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer

    server = HTTPServer(('', PORT_NUMBER), JsonHandler)
    try:
        print 'started http server on --> %s:%s%s' % (getIPAddress(), PORT_NUMBER, API_REGULAR)
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
