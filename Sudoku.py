from flask import Flask, render_template, request, redirect, flash, url_for, session
import database as db

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
app.secret_key = 'secret key'

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET' :
        return render_template('login.html', msg = None)


@app.route('/login', methods=['POST'])
def log_in() :
    pw = db.user_login(request.form.get('username', None))
    if pw == request.form.get('password') :
        session['username'] = request.form.get('username', None)
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
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)
