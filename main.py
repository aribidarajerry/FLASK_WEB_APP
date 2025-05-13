from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error=e), 500







if __name__=='__main__':
    app.run(debug=True)