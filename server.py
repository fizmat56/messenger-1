from flask import Flask
import time

app = Flask(__name__)
myChatName = 'FM56chat 1.0'

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return {
        'status': True,
        'name': myChatName,
        'time': time.asctime()
    }

app.run()
