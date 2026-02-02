from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'timestamp': time.time()})

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulate database query
    time.sleep(random.uniform(0.01, 0.1))
    return jsonify({
        'data': [random.randint(1, 1000) for _ in range(10)],
        'timestamp': time.time()
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'DDoS Protected API', 'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
