
import streamlit as st
import spacy
from spacy import displacy

st.title('Named Entity Recognition')

text = st.text_area('Input Text Here...')

nlp_model = spacy.load('en_core_web_sm')

if text: #true
    doc = nlp_model(text)
    # st.write(doc)

    html_page = displacy.render(doc, style = 'ent')
    st.write(html_page, unsafe_allow_html = True)


# import subprocess
# import sys

# subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

# try:
#     import spacy
#     nlp = spacy.load("en_core_web_sm")
#     print("Model already installed!")
# except OSError:
#     print("Model not found. Installing...")
#     from spacy.cli import download
#     download("en_core_web_sm")
#     nlp = spacy.load("en_core_web_sm")
#     print("Model installed and loaded successfully!")
