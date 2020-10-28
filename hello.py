from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/<name>')s
def nameUser(name):
    return f"<h1>Hello {name}!</h1>",200

if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)