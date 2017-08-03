from flask import Flask
from flask_ask import Ask, statement, question
import random as rand
import requests
import time
import unidecode
import json

app = Flask(__name__)
ask = Ask(app, '/')

goodbyeMsg = []
goodbyeMsg[0] = "Later Nerds!"
goodbyeMsg[1] = "Okay, then. I see how it is."
goodbyeMsg[2] = "

@app.route('/')
def homepage():
    """
    When Alexa starts, she will say "Hello"
    """
    return "Hello"

@ask.launch
def start_skill():
    """
    """
    msg = "Are you ready to get roasted?"
    return question(msg)

@ask.intent("YesIntent")
def get_rekt():
    """
    """
    roast_msgs = []

    with open('roasts.txt', 'r') as file:
        for line in file:
            roast_msgs.append(line.strip())
    random = round(rand.random() * len(roast_msgs))
    roast_msg = roast_msgs[random]

    return statement(roast_msg)

@ask.intent("NoIntent")
def no_intent():
    """
    """
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)