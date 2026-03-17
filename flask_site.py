from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index Page</h1>"

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<user_name>')
def hello(user_name=None):
    # if user_name:
    #     return f"<h1>hi, {escape(user_name)}! jejej</h1>"
    # else:
    #     return "<h1>hi, world! jejej</h1>"
    return render_template('home.html', user=user_name)