from flask import Flask, render_template
from translate import Translator


app = Flask(__name__)

dictobjs={}


@app.route('/')
def home():
    return ''

@app.route('/traduzir/<lfrom>/<lto>/<frase>')
def traduzir(lfrom,lto,frase):


    translator = Translator(from_lang=lfrom, to_lang=lto)
    translation = translator.translate(frase)

    return translation

#app.run()


