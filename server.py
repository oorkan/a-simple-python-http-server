# server.py
from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='public', **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        if self.path == '/lyrics':
            self.path = '/lyrics.html'

        return super().do_GET()


class Server:
    def __init__(self,
                 server_address=('127.0.0.1', 0),
                 handler=SimpleHTTPRequestHandler):
        self.server_address = server_address
        self.handler = handler

    def serve(self):
        with TCPServer(self.server_address, self.handler) as httpd:
            serving_at = httpd.server_address

            print(f'serving at http://{serving_at[0]}:{serving_at[1]}')
            httpd.serve_forever()


server = Server(handler=Handler)
server.serve()
