from flask import Flask, render_template, request, redirect, flash, url_for, session
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
def log_in() :
    username = request.form.get('username', None)
    pw = db.user_login(username)
    if (not pw) :
        flash('Incorrect username!')
        return redirect(url_for('index'))

    if pw == request.form.get('password', None) :
        session['username'] = username
        return redirect('/main')

    flash("wrong login info")
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET' :
        return render_template('signup.html')
    else :
        username = request.form.get('username', None)
        fullname = request.form.get('fullname', None)
        password = request.form.get('password', None)
        db.add_user(username, password, fullname)
        return redirect('/')

@app.route('/main')
def game_page():
    if 'username' not in session :
        flash('log in first to play Sudoku!')
        return redirect(url_for('index'))
    board = game.get_game(1)
    return render_template('game.html', board=board)


if __name__ == '__main__':
    app.run(debug=True)
