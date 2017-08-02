from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from collections import OrderedDict
import requests
import pickle
import unidecode
import json
import numpy as np

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
   return "Hello World!"

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
def get_stock(company):
    print("get ticker")
    ticker = name_to_ticker(company.lower())
    return statement(output(ticker))

def name_to_ticker(company):
    ticker_dict = pickle.load(open('ticker_dict.pickle', 'rb'))
    return ticker_dict[company]


def output(ticker):
    """
    Using AlphaVantage, calculates current price of ticker and daily %change
    
    Parameters
    ---------------
    ticker(string): The chosen stock ticker
    
    Returns
    --------------
    Returns a string to be read by Alexa reporting the price and change of the ticker
    """

    # Anthony Cavallaro's AlphaVantage API Key. Used to get stock info in JSON format.
    apikey = GXTRIS3LY4DDIF3S

    # URL used to get the JSON file
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=compact&apikey={}'.format(
        ticker, apikey)

    # Loads information in JSON format from URL as a dictionary
    sess = requests.Session()
    html = sess.get(url)
    time_series_day = json.loads(html.content.decode('utf-8'))

    # Prunes metadata from the time_series_day data
    time_series_day = time_series_day["Time Series (Daily)"]

    # Constructs a sorted ordered dictionary
    ordered = OrderedDict(sorted(time_series_day.items(), key=lambda t: t[0], reverse=True))

    # Gets the top two values, stores in a list
    count = 0
    values = []
    for key in ordered:
        values.append(ordered[key]['4. close'])
        count += 1
        if count == 2:
            break

    # Top two values, current price and previous close
    current_price = float(values[0])
    prev_close = float(values[1])

    # Calculates percent change on the day of the stock
    percent_change = np.round(abs(prev_close - current_price) / prev_close * 100, 2)

    # Report to be read by Alexa
    return "The price of {} is currently {}, and changed {} percent from yesterday".format(ticker, current_price, percent_change)

if __name__=='__main__':
   app.run(debug=True)