from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import requests
import unidecode
import json

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome = render_template('stock_open')
    reprompt = render_template('stock_again')
    return question(welcome) \
        .reprompt(reprompt)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def quit_stocks():
    quit_app = render_template('stock_quit')
    return statement(quit_app)

@ask.intent('GetStockIntent')
def get_stock():
    #Implementing once AJ finishes code
    return statement("You've reached the stock intent zone.")



