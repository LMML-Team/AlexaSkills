from flask import Flask, render_template
from flask_ask import Ask, question, statement
import Generate_text as gt
import pickle

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    pass

@ask.launch
def start_skill():
    lm = pickle.load( open("alternative_facts.p", "rb"))

    out = gt.generate_text(lm, 11, nletters=1000)
    return statement(out)

if __name__ == '__main__':
    app.run(debug=True)