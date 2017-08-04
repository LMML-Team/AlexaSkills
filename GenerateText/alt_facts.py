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
    string = pickle.load( open("wiki_data.p", "rb"))
    lm_order = 11
    lm = gt.train_lm(string, lm_order)
    out = gt.generate_text(lm, lm_order, nletters=100)
    return statement(out)

if __name__ == '__main__':
    app.run(debug=True)