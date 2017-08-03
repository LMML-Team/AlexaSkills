from flask import Flask, render_template
from flask_ask import Ask, question, statement
import face_recognition as fr

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hello"

@ask.launch
def start_skill():
    msg = render_template('fr_open')
    return question(msg) \
        .reprompt(msg)

@ask.intent('AMAZON.YesIntent')
def take_pic():
    print(fr.add_picture(alexa=True))

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def quit():
    return statement("See ya")

if __name__ == '__main__':
    app.run(debug=True)