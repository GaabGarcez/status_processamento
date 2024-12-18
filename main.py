from flask import Flask, jsonify, Response
import psutil
import time
import threading

app = Flask(__name__)

# Variáveis globais para armazenar o uso de CPU e RAM
cpu_usage = 0
ram_usage = 0

# Função para atualizar o uso de CPU e RAM periodicamente
def update_usage():
    global cpu_usage, ram_usage
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Percentual de uso da CPU
        ram_usage = psutil.virtual_memory().percent  # Percentual de uso da RAM
        time.sleep(1)  # Atualiza a cada 1 segundo

# Iniciar a thread para monitorar os recursos
thread = threading.Thread(target=update_usage)
thread.daemon = True
thread.start()

@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({
        'cpu_usage': f"{cpu_usage}%",
        'ram_usage': f"{ram_usage}%"
    })

@app.route('/')
def home():
    return Response("<h1>Monitor de CPU e RAM</h1><p>Use o endpoint <code>/metrics</code> para acessar os dados.</p>", mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
