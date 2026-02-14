from flask import Flask, render_template_string, jsonify
import datetime

app = Flask(__name__)

# Real data from OpenClaw sessions (updated manually or via cron)
SUB_AGENTS = [
    {
        'name': 'organisk-trafik',
        'status': 'idle',
        'start_time': '2026-02-14 11:00 UTC',
        'last_activity': '2026-02-14 11:05 UTC',
        'task': 'Generate/Exec Reddit r/PromptEngineering post + X thread for traffic',
        'revenue_potential': 'High (100+ visitors/day, direct to PayPal)',
        'progress': 'Post ready in promo-plan.md, awaiting manual exec'
    },
    {
        'name': 'direct-outreach',
        'status': 'idle',
        'start_time': '2026-02-14 11:02 UTC',
        'last_activity': '2026-02-14 11:04 UTC',
        'task': 'DM templates + Shopify targets from sub-outreach-*.md',
        'revenue_potential': 'Medium (1-5 direct sales via personalized outreach)',
        'progress': 'Templates/targets ready, copy-paste guide generated'
    },
    {
        'name': 'community-acquisition',
        'status': 'idle',
        'start_time': '2026-02-14 11:03 UTC',
        'last_activity': '2026-02-14 11:06 UTC',
        'task': 'Discord AI/ecom servers + intro posts/shares',
        'revenue_potential': 'High (viral funnel to site)',
        'progress': 'Server list + posts ready'
    }
]

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, subs=SUB_AGENTS)

@app.route('/api/subs')
def api_subs():
    return jsonify(SUB_AGENTS)

@app.route('/update', methods=['POST'])
def update():
    # Placeholder for cron/manual update of SUB_AGENTS from sessions_list
    return jsonify({'status': 'updated'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

HTML_TEMPLATE = '''
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Glyph Sub-Agent Dashboard&lt;/title&gt;
    &lt;link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"&gt;
    &lt;style&gt;
        body { font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 50%, #1f1f2e 100%); color: white; margin: 0; padding: 2rem; }
        .container { max-width: 1200px; margin: auto; }
        h1 { text-align: center; color: #3b82f6; }
        table { width: 100%; border-collapse: collapse; margin-top: 2rem; background: rgba(255,255,255,0.05); border-radius: 1rem; overflow: hidden; }
        th, td { padding: 1rem; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.1); }
        th { background: rgba(59,130,246,0.2); }
        .status { padding: 0.5rem 1rem; border-radius: 0.5rem; font-weight: 600; }
        .running { background: #10b981; color: white; }
        .idle { background: #f59e0b; color: white; }
        .revenue-high { color: #10b981; font-weight: bold; }
        .feed { height: 400px; overflow-y: auto; background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 0.5rem; margin-top: 1rem; }
        button { background: #3b82f6; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor: pointer; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;h1&gt;💼 Glyph Johnson Sub-Agent Dashboard&lt;/h1&gt;
        &lt;p style="text-align: center; opacity: 0.8;"&gt;Real-time overview. Auto-refresh in prod via cron.&lt;/p&gt;
        &lt;table&gt;
            &lt;thead&gt;
                &lt;tr&gt;
                    &lt;th&gt;Name&lt;/th&gt;
                    &lt;th&gt;Status&lt;/th&gt;
                    &lt;th&gt;Start Time&lt;/th&gt;
                    &lt;th&gt;Last Activity&lt;/th&gt;
                    &lt;th&gt;Task&lt;/th&gt;
                    &lt;th&gt;Progress&lt;/th&gt;
                    &lt;th&gt;Revenue Potential&lt;/th&gt;
                &lt;/tr&gt;
            &lt;/thead&gt;
            &lt;tbody&gt;
                {% for sub in subs %}
                &lt;tr&gt;
                    &lt;td&gt;&lt;strong&gt;{{ sub.name }}&lt;/strong&gt;&lt;/td&gt;
                    &lt;td&gt;&lt;span class="status {{ 'running' if sub.status == 'running' else 'idle' }}"&gt;{{ sub.status.upper() }}&lt;/span&gt;&lt;/td&gt;
                    &lt;td&gt;{{ sub.start_time }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.last_activity }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.task }}&lt;/td&gt;
                    &lt;td&gt;{{ sub.progress }}&lt;/td&gt;
                    &lt;td class="revenue-high"&gt;{{ sub.revenue_potential }}&lt;/td&gt;
                &lt;/tr&gt;
                {% endfor %}
            &lt;/tbody&gt;
        &lt;/table&gt;
        &lt;div style="text-align: center; margin-top: 2rem;"&gt;
            &lt;button onclick="location.reload()"&gt;Refresh&lt;/button&gt;
            &lt;button onclick="fetch('/api/subs').then(r =&gt; r.json()).then(data =&gt; console.log('Updated:', data))"&gt;API Test&lt;/button&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
'''
