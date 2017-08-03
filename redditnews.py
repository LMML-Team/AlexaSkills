from flask import Flask
from flask_ask import Ask, statement, question
import requests
import time
import unidecode
import json

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    """
    When Alexa starts, she will say "Hello"
    """
    return "Hello"

@ask.launch
def start_skill():
    """
    When you say the keywords, she will say "Would you like to hear the news?"
    """
    msg = "Would you like to hear the news?"
    return question(msg)

def get_headlines():
    """
    Returns the titles of the top 5 articles from the reddit feed URL.
    """
    user_cred = {'user': 'cogworks2017',
                 'passwd': 'beaverworks',
                 'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'cogworks'})
    sess.post('https://www.reddit.com/api/login', data=user_cred)

    url = 'https://reddit.com/r/worldnews/.json?limit=5'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(x['data']['title']) for x in data['data']['children']]
    titles = "... ".join(titles)
    return titles

@ask.intent("YesIntent")
def share_headlines():
    """
    When you answer yes after Alexa asked , it will return the message with the headlines
    """
    headlines = get_headlines()
    headlines_msg = "The current world news headlines are, {}".format(headlines)
    return statement(headlines_msg)

@ask.intent("NoIntent")
def no_intent():
    """
    When you say no after Alexa, it will say "Ok, thanks. Have a nice day."
    """
    msg = "Ok, thanks. Have a nice day."
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)