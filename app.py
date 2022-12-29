from flask import Flask

app = Flask(__name__)

def print(num):
    return print(num)


@app.route('/')
def hello_world():
    return 'Hello, World!'
