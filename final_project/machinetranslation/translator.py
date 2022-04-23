"""
Imports Language translator from IBM service and codes for translation en-fr and fr-en.
"""
import json

import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_disable_ssl_verification(True)

language_translator.set_service_url(
    'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/09074670-8c5c-4dcc-8259-25dc658ac122')



def english_to_french(english_text):
    '''translates english input text to french output'''
    translation= language_translator.translate(
        text=english_text, model_id="en-fr").get_result()
    french_text= translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''translates french input text to english output'''
    translation= language_translator.translate(
        text=french_text, model_id="fr-en").get_result()
    english_text= translation['translations'][0]['translation']
    return english_text
