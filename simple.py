from flask import Flask

app = Flask(__name__)
app.config['greeting']='Hello, world!'

@app.route('/')
def hello():
    return f'<h1>{app.config["greeting"]}</h1>'