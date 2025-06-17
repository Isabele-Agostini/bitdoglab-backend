from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.json
    print(f"[{datetime.now()}] Dados recebidos:")
    print(dados)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run()
