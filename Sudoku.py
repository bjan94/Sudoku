from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/main')
def game_page():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)
