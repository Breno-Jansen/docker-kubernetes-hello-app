
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        mensagem = "Breno Jansen - Projeto Interdisciplinar para Sistemas de Informação IV"
        self.wfile.write(mensagem.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8080), MyHandler)

print("Servidor rodando em http://localhost:8080", flush=True)
server.serve_forever()