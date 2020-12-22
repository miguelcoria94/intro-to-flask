from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/home')
def home():
    return f'<h1>Home</h1>'

@app.route('/about')
def about():
    return '<h1>About</h1>'

@app.route('/item/<int:id>')
def item(id):
    return f'<h1>Item {id}</h1>'

@app.before_request
def before_request_function():
    print("before_request is running")


@app.after_request
def after_request_function(response):
    print("after_request is running")
    return response


@app.before_first_request
def before_first_function():
    print("before first request")

