from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def landing():
    return jsonify({"message": "Hello!"})

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from the Flask backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
