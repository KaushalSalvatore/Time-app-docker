from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import time

app = Flask(__name__)

# Timer state
timer_state = {
    'running': False,
    'paused': False,
    'start_time': None,
    'paused_duration': 0,
    'last_pause_time': None,
    'total_duration': 600  # 10 minutes in seconds
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_timer():
    if not timer_state['running']:
        timer_state['running'] = True
        timer_state['paused'] = False
        timer_state['start_time'] = time.time()
        timer_state['paused_duration'] = 0
        timer_state['last_pause_time'] = None
    return jsonify({'status': 'started'})

@app.route('/pause')
def pause_timer():
    if timer_state['running'] and not timer_state['paused']:
        timer_state['paused'] = True
        timer_state['last_pause_time'] = time.time()
    return jsonify({'status': 'paused'})

@app.route('/resume')
def resume_timer():
    if timer_state['running'] and timer_state['paused']:
        # Calculate how long we were paused
        pause_duration = time.time() - timer_state['last_pause_time']
        timer_state['paused_duration'] += pause_duration
        timer_state['paused'] = False
        timer_state['last_pause_time'] = None
    return jsonify({'status': 'resumed'})

@app.route('/stop')
def stop_timer():
    timer_state['running'] = False
    timer_state['paused'] = False
    timer_state['start_time'] = None
    timer_state['paused_duration'] = 0
    timer_state['last_pause_time'] = None
    return jsonify({'status': 'stopped'})

@app.route('/status')
def get_status():
    if not timer_state['running']:
        return jsonify({
            'running': False,
            'paused': False,
            'remaining': timer_state['total_duration'],
            'formatted': format_time(timer_state['total_duration'])
        })
    
    if timer_state['paused']:
        elapsed = timer_state['last_pause_time'] - timer_state['start_time'] - timer_state['paused_duration']
    else:
        elapsed = time.time() - timer_state['start_time'] - timer_state['paused_duration']
    
    remaining = max(timer_state['total_duration'] - elapsed, 0)
    
    return jsonify({
        'running': timer_state['running'],
        'paused': timer_state['paused'],
        'remaining': remaining,
        'formatted': format_time(remaining)
    })

def format_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    app.run(debug=True)