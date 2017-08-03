"""Hello - need to update this description."""
import audio_identification as ai
import numpy as np

#Flask Imports
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
ask = Ask(app, '/')

@app.route("/")
def homepage():
    
    return "Hello"

from app import app
@app.route('/')
@app.route('/index')
def webpage():
    return '''
    <html>
    <head>

    </head>
    <body>
    <h1>Hello</h1>
    <input type="file" accept="image/*;capture=camera">

    </body>
    </html>
    '''
@ask.launch
def start_skill():
    """
    """
    return question("Would you like to identify some sick beats?")

@ask.intent("YesIntent")
def begin_recording():
    """
    """
    return statement("Please play the song for 10 seconds. Now recording.")
    msg = record_song()
    return statment("I think the songs were {}, {}, and {}".format(msg[0], msg[1], msg[2]))

@ask.intent("NoIntent")
def no_intent():
    """
    """
    return statement("Okay. Thanks.")


if __name__=="__main__":
        app.run(host='0.0.0.0', port=80, debug=True)