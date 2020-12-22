from flask import (Flask, render_template, redirect)
from config import Config
from sample_form import SampleForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    nav = [
        {'href': 'https://appacademy.io', 'caption': 'App Academy'},
        {'href': 'https://archive.or', 'caption': 'Internet Archive'},
    ]
    return render_template('index.html', sitename="JustStocks", navigation=nav)


@app.route('/about')
def about():
    return render_template('index.html', sitename='My Sample', page="About")
@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('form.html', form=form)

