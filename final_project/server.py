'''
Routing for translator app and flask webbuild
'''
import json
from flask import Flask, render_template, request
import machinetranslation
from machinetranslation import translator

app = Flask("Web Translator")

@app.route('/translate_to_french')
def translate_to_french():
    '''routes button translate to french'''
    text_to_translate = request.args.get('textToTranslate')
    english_text= translator.english_to_french(text_to_translate)
    return english_text

@app.route('/translate_to_english')
def translate_to_english():
    '''routes button translate to english'''
    text_to_translate = request.args.get('textToTranslate')
    french_text= translator.french_to_english(text_to_translate)
    return french_text

@app.route('/')
def render_index_page():
    '''routes index page'''
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
