from flask import (Flask, render_template)
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    nav = [
        {'href': 'https://appacademy.io', 'caption': 'App Academy'},
        {'href': 'https://archive.or', 'caption': 'Internet Archive'},
    ]
    return render_template('index.html', sitename="JustStocks", navigation=nav)

