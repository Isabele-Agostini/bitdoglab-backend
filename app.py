from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.json
    print(f"[{datetime.now()}] Dados recebidos:")
    print(dados)
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
