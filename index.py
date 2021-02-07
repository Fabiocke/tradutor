from flask import Flask, render_template
from googletrans import Translator


app = Flask(__name__)

dictobjs={}



@app.route('/<frase>')
def traduzir(frase):
    translator = Translator()
    detec=translator.detect(frase).lang
    destino = 'pt' if detec!='pt' else 'en'
    translation = translator.translate(frase, dest=destino)
    return translation.text



