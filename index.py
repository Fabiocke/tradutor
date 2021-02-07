from flask import Flask, render_template
from translate import Translator
from langdetect import detect


app = Flask(__name__)

dictobjs={}


@app.route('/')
def home():
    return ''

@app.route('/traduzir/<frase>')
def traduzir(frase):


    translator = Translator(from_lang='pt', to_lang='en')
    translation = translator.translate(frase)

    return translation

#app.run()


