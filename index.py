from flask import Flask, render_template
from googletrans import Translator


app = Flask(__name__)


@app.route('/')
def home():
    return ''

@app.route('/traduzir/<frase>')
def traduzir(frase):
    
    translator = Translator()
    return frase
    detec=translator.detect(frase).lang
    destino = 'pt' if detec!='pt' else 'en'
    translation = translator.translate(frase, dest=destino)
    
    return translation.text

#app.run()



