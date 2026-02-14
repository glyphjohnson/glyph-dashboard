from flask import Flask, render_template_string, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = 'data'

HTML_TEMPLATE = '''
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Glyph Sub-Agent Dashboard&lt;/title&gt;
    &lt;style&gt;
        body { font-family: Inter, sans-serif; background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 50%, #1f1f2e 100%); color: white; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: auto; }
        h1 { text-align: center; color: #3b82f6; }
        .subtitle { text-align: center; opacity: 0.8; }
        table { width: 100%; border-collapse: collapse; margin-top: 2rem; background: rgba(255,255,255,0.05); border-radius: 1rem; overflow: hidden; }
        th, td { padding: 1rem; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }
        th { background: rgba(59,130,246,0.2); }
        .status { padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600; }
        .running { background: #10b981; color: white; }
        .idle { background: #f59e0b; color: white; }
        .revenue-high { color: #10b981; font-weight: bold; }
        .controls { text-align: center; margin-top: 2rem; }
        button { background: #3b82f6; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 0.5rem; cursor: pointer; margin: 0 0.5rem; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;h1&gt;💼 Glyph Johnson Sub-Agent Dashboard&lt;/h1&gt;
        &lt;p class="subtitle"&gt;Live data. Last update: {{ last_update }} | Total: {{ total_subs }} | Active: {{ active_subs }}&lt;/p&gt;
        &lt;table&gt;
            &lt;thead&gt;
                &lt;tr&gt;
                    &lt;th&gt;Name&lt;/th&gt;
                    &lt;th&gt;Status&lt;/th&gt;
                    &lt;th&gt;Start&lt;/th&gt;
                    &lt;th&gt;Last&lt;/th&gt;
                    &lt;th&gt;Task&lt;/th&gt;
                    &lt;th&gt;Progress&lt;/th&gt;
                    &lt;th&gt;Revenue&lt;/th&gt;
                &lt;/tr&gt;
            &lt;/thead&gt;
            &lt;tbody&gt;
                {% for sub in subs %}
                &lt;tr&gt;
                    &lt;td&gt;{{ sub.name }}&lt;/td&gt;
                    &lt;td&gt;&lt;span class="status {{ sub.status.lower() }}"&gt;{{ sub.status.upper() }}&lt;/span&gt;&lt;/td&gt;
                    &lt;td&gt;{{ sub.start_time }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.last_activity }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.task }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.progress }}&lt;/td&gt;
                    &lt;td class="revenue-high"&gt;{{ sub.revenue_potential }}&lt;/td&gt;
                &lt;/tr&gt;
                {% endfor %}
            &lt;/tbody&gt;
        &lt;/table&gt;
        &lt;div class="controls"&gt;
            &lt;button onclick="location.reload()"&gt;Refresh&lt;/button&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
'''

def load_data(filename, default):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return default

@app.route('/')
def dashboard():
    subs = load_data('subs.json', [])
    meta = load_data('meta.json', {'last_update': datetime.now().strftime('%Y-%m-%d %H:%M UTC'), 'total_subs': len(subs), 'active_subs': 0})
    return render_template_string(HTML_TEMPLATE, subs=subs, last_update=meta['last_update'], total_subs=meta['total_subs'], active_subs=meta['active_subs'])

@app.route('/api/subs')
def api_subs():
    return jsonify(load_data('subs.json', []))

@app.route('/api/meta')
def api_meta():
    return jsonify(load_data('meta.json', {}))

if __name__ == '__main__':
    os.makedirs(DATA_DIR, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
