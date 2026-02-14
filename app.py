from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = 'data'

@app.route('/')
def dashboard():
    subs = load_data('subs.json', [])
    meta = load_data('meta.json', {'last_update': 'No data', 'total_subs': 0, 'active_subs': 0})
    return render_template('dashboard.html', subs=subs, last_update=meta['last_update'], total_subs=meta['total_subs'], active_subs=meta['active_subs'])

@app.route('/api/subs')
def api_subs():
    return jsonify(load_data('subs.json', []))

@app.route('/api/meta')
def api_meta():
    return jsonify(load_data('meta.json', {}))

def load_data(filename, default):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return default

if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=8080, debug=False)
