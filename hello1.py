import pickle
from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ping")
def pinger():
    return {'Message' : 'Hi I am pinging.............'}
