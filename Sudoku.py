from flask import Flask, render_template, request, redirect, \
    flash, url_for, session, json, jsonify
import database as db
import Game as game

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = 'secret key'

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET' :
        return render_template('login.html', msg=None)


@app.route('/login', methods=['POST'])
def log_in():
    username = request.form.get('username', None)
    user_info = db.user_login(username)
    if (not user_info):
        flash('Incorrect username!')
        return redirect(url_for('index'))

    if user_info['password'] == request.form.get('password', None):

        session['username'] = user_info['user']
        session['name'] = user_info['fullname']
        session['progress'] = user_info['progress']
        return redirect('/main')

    flash("wrong login info")
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET' :
        return render_template('signup.html')
    else :
        username = request.form.get('username', None)
        fullname = request.form.get('name', None)
        password = request.form.get('password', None)
        if (username != None and fullname != None and password != None) :
            db.add_user(username, password, fullname)
            session['username'] = username
            session['name'] = fullname
            session['progress'] = '0'
            return redirect('/main')

        flash("you must complete all of the fields")
        return redirect(url_for('sign_up'))


@app.route('/main')
def game_page():
    if 'username' not in session :
        flash('log in first to play Sudoku!')
        return redirect(url_for('index'))

    # board = game.get_game(1)
    board = game.game_generator(int(session['progress']))
    print(board)
    return render_template('game.html',
                           fullname=session['name'], board=board)

@app.route('/validate', methods=['POST'])
def validate():
    i = int(request.form['i'])
    j = int(request.form['j'])
    val = int(request.form['val'])

    if game.is_valid(i, j, val):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route('/puzzleSolved', methods=['GET'])
def get_next_puzzle():
    if 'username' not in session:
        redirect(url_for('index'))
    nextLevel = int(session['progress']) + 1
    session['progress'] = nextLevel
    db.updateLevel(session['username'], str(nextLevel))
    return redirect(url_for('game_page'))


@app.route('/gethint', methods=['POST'])
def hint():
    i = int(request.form['i'])
    j = int(request.form['j'])

    solved = game.return_solved()

    return jsonify(answer=str(solved[i][j]))


@app.route('/logout', methods=['GET'])
def log_out():
    if 'username' not in session:
        return redirect(url_for('index'))
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
