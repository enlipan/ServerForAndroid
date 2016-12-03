# coding=utf-8
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

PORT_NUM = 7777


class SimpleRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        return

    def do_HEAD(self):
        return


if __name__ == '__main__':
    simpleServer = HTTPServer(('', PORT_NUM), SimpleRequestHandler)
    simpleServer.serve_forever()
