from flask import Flask, jsonify
import json

app = Flask(__name__)
latest_telemetry = {"altitude": 0, "velocity": 0, "temperature": 0}

@app.route('/telemetry')
def get_telemetry():
    return jsonify(latest_telemetry)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
