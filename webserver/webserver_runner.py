"""
Basic webserver that returns a text string on the port 8000
Can be closed by Ctrl+C
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

from webserver.response import get_response


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = get_response()
        self.wfile.write(response)


def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Server is closed')

