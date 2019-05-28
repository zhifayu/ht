from http.server import HTTPServer,BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_sth_for_GET(self):
        self.send_response(200)
        self.send_header('Content_type','text/plain;charset = utf-8')
        self.end_header()

        self.wfile.write('hello everyone,i am ht\n',encode())

if __name__ == 'main':
    server_address = ('',9999)
    httpd = HTTPServer(server_address.Handler)
    httpd.serve_forever()
    