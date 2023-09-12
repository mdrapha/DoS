from http.server import BaseHTTPRequestHandler, HTTPServer
import time


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")
        print(
            f"Received request from: {self.client_address[0]}:{self.client_address[1]}"
        )

    def log_message(self, format, *args):
        # Suprimindo a saída de log padrão
        return


def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    addr="127.0.0.1",
    port=80,
):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
