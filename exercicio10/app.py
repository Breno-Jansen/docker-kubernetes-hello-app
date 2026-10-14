from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

NOME_ALUNO = "Breno Jansen"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data_atual = datetime.now().strftime("%d/%m/%Y")
        mensagem = f"{NOME_ALUNO} - Data atual: {data_atual}"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(mensagem.encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8080), MyHandler)

print("Servidor iniciado na porta 8080", flush=True)
server.serve_forever()
