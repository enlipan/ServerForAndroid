from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 7777

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("Hello Word")
        return

try:
    server = HTTPServer(('',PORT_NUMBER),MyHandler)
    print 'started http server on port', PORT_NUMBER
    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()