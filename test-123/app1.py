from flask import Flask

app = Flask(__name__)

def print(num):
    return print(num)
    
def print1():
    return print()


@app.route('/')
def hello_world():
    return 'Hello, World!'