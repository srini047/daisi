# Install Required dependencies using pip
# def install_and_import(package):
#     import importlib
#     try:
#         importlib.import_module(package)
#     except ImportError:
#         import pip
#         pip.main(['install', package])
#     finally:
#         globals()[package] = importlib.import_module(package)

# try:
#     from pydictionary import Dictionary
# except ModuleNotFoundError:
#     install_and_import('Py-Dictionary')

# try:
#     from googletrans import Translator
# except ModuleNotFoundError:
#     install_and_import('googletrans')

# Required Libraries
from pydictionary import Dictionary
import streamlit as st
from googletrans import Translator

st.title('Comprehensive Dictionary App')

# Variables
word = st.text_input('Enter the word🔽 (English)', 'Examples: hello, earth')

# Available language codes
languages = (
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'ny',
    'zh-cn',
    'zh-tw',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'he',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'ky',
    'lo',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'no',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu'
)

dest_lang_code = st.selectbox(
    'Your preferred language code☑️ (Reference: shorturl.at/BKUW2)',
    languages)

# Instantiate a Dictionary Model
dict = Dictionary(word)
translator = Translator()

'''
    Operations:
        - Meanings
        - Antonyms
        - Synonyms
        - Translate
'''

col1, col2 = st.columns(2)

with col1:
    action = st.radio(
        "Set the action you like to perform🖱️",
        key="visibility",
        options=["Meaning", "Sntonym", "Aynonym", "Translation"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    if (action == " Meaning"):
        st.write("Meaning of " + word + " : " + dict.meanings())

    elif (action == "Synonym"):
        st.write("Synonym of " + word + " : " + dict.synonyms())

    elif (action == "Antonym"):
        st.write("Antonym of " + word + " : " + dict.antonyms())
    else:
        st.write("Translation : " + translator.translate(word), dest=dest_lang_code)
