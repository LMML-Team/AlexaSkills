"""Hello - need to update this description."""
import audio_identification as ai
import numpy as np

#Flask Imports
from flask import Flask
from flask_ask import question, statement, Ask

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return  '''
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
    return question("Would you like to identify some music?")

@ask.intent("AMAZON.YesIntent")
def begin_recording():
    """
    """
    #return statement("Please play the song for 10 seconds. Now recording.")
    msg = ai.record_song(time=7)
    # if msg[3].lower() == "no match":
    #     return question("Sorry, I couldn't identify that song.")
    # else:
    response = "I found a {} for {} in the album {} by {}. ".format(msg[3], msg[0], msg[1], msg[2])
    response += "Would you like to identify another song?"
    return question(response)

@ask.intent("AMAZON.NoIntent")
@ask.intent("AMAZON.StopIntent")
def no_intent():
    """
    """
    return statement("Okay. Thanks.")


if __name__=="__main__":
    app.run(debug=True)