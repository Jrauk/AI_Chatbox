'''
Routing for translator app and flask webbuild
'''
import json
from flask import Flask, render_template, request
import machinetranslation
from machinetranslation import translator

app = Flask("Web Translator")

@app.route('/english_to_french')
def english_to_french():
    '''routes button translate to french'''
    english_text = request.args.get('text_to_translate')
    return translator.english_to_french(english_text)

@app.route('/french_to_english')
def french_to_english():
    '''routes button translate to english'''
    french_text = request.args.get('text_to_translate')
    return translator.french_to_english(french_text)

@app.route('/')
def render_index_page():
    '''routes index page'''
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
