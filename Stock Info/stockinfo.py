from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import requests
import unidecode
import json
import numpy as np

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

def output(ticker):
    sess = requests.Session()
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=compact&apikey=GXTRIS3LY4DDIF3S'.format(
        ticker)
    html = sess.get(url)

    time_series_day = json.loads(html.content.decode('utf-8'))
    days = time_series_day['Time Series (Daily)']
    ordered = OrderedDict(sorted(days.items(), key=lambda t: t[0], reverse=True))

    count = 0
    values = []
    for key in ordered:
        values.append(ordered[key]['4. close'])
        count += 1
        if count == 2:
            break

    current_price = float(values[0])
    prev_close = float(values[1])
    percent_increase = np.round(abs(prev_close - current_price) / prev_close * 100, 2)

    return "The price of {} is currently {}, and is up {} percent today/".format(ticker, current_price, percent_increase)


