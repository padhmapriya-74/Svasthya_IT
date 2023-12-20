from flask import Flask, request, render_template, redirect, url_for, request, jsonify

from flask_socketio import SocketIO
import subprocess
app = Flask(__name__)

# Route to the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacman')
def pacman():
    return render_template('pacman-index.html')

@app.route('/diet_plan')
def diet_plan():
    return render_template('diet-index.html')

@app.route('/child_index')
def child_index():
    return render_template('child_index.html')

@app.route('/ma_index')
def ma_index():
    return render_template('ma_index.html')

@app.route('/old_index')
def old_index():
    return render_template('old_index.html')

@app.route('/child_physical_page')
def child_physical_page():
    return render_template('child_physical_page.html')

@app.route('/child_mental_page')
def child_mental_page():
    return render_template('child_mental_page.html')

@app.route('/child_ar')
def child_ar():
    return render_template('child_ar.html')

@app.route('/child_culture')
def child_culture():
    return render_template('child_culture.html')

@app.route('/child_hygiene')
def child_hygiene():
    return render_template('child_hygiene.html')

@app.route('/ma_physical_page')
def ma_physical_page():
    return render_template('ma_physical_page.html')

@app.route('/ma_mental_page')
def ma_mental_page():
    return render_template('ma_mental_page.html')

@app.route('/ma_ar')
def ma_ar():
    return render_template('ma_ar.html')

@app.route('/ma_culture')
def ma_culture():
    return render_template('ma_culture.html')

@app.route('/ma_hygiene')
def ma_hygiene():
    return render_template('ma_hygiene.html')

@app.route('/ma_reflexology')
def ma_reflexology():
    return render_template('ma_reflexology.html')

@app.route('/ma_yoga')
def ma_yoga():
    return render_template('ma_yoga.html')


@app.route('/old_physical_page')
def old_physical_page():
    return render_template('old_physical_page.html')

@app.route('/old_mental_page')
def old_mental_page():
    return render_template('old_mental_page.html')

@app.route('/old_ar')
def old_ar():
    return render_template('old_ar.html')

@app.route('/old_culture')
def old_culture():
    return render_template('old_culture.html')


@app.route('/old_reflexology')
def old_reflexology():
    return render_template('old_reflexology.html')

@app.route('/old_yoga')
def old_yoga():
    return render_template('old_yoga.html')

@app.route('/memory_game')
def memory_game():
    return render_template('memory-index.html')

@app.route('/tower_block')
def tower_block():
    return render_template('tower-index.html')

@app.route('/guess_word')
def guess_word():
    return render_template('guess-index.html')

@app.route('/reflexology_click')
def reflexology_click():
    return render_template('reflexology-index.html')

@app.route('/reflexology_new')
def reflexology_new():
    return render_template('reflexology-new.html')

@app.route('/drag_drop')
def drag_drop():
    return render_template('dragdrop-index.html')

@app.route('/anatomy')
def anatomy():
    return render_template('anatomy.html')

socketio = SocketIO(app)



# Route to start the game
@app.route('/play_game')
def play_game():
    socketio.emit('game_result', {'result': 'Game started!'}, namespace='/game')
    subprocess.Popen(['python', 'pacman.py'])
    return ''

# SocketIO event handler for game results
@socketio.on('game_result', namespace='/game')
def handle_game_result(data):
    print(data['result'])

@app.route('/img_puzzle')
def img_puzzle():
    return render_template('img_puzzle-index.html')

@app.route('/dial')
def dial():
    return render_template('dial-index.html')
@app.route('/run_game', methods=['POST'])
def run_game():
    # Run the game.py script using subprocess
    subprocess.run(['python', 'game.py'])
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)