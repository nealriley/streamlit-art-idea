import numpy as np
import streamlit as st
import time
from content.demo import stream_data, stream_words


CONTENT_CHOICES=[stream_data, stream_words]

page_container = st.empty()

def content(page):
    page_container.empty()
    time.sleep(.4)
    body = page_container.container()
    with body:
        st.write_stream(page)

def generate():
    # choose a random option from all available options in CONTENT_CHOICES array
    option=np.random.choice(len(CONTENT_CHOICES))
    return(CONTENT_CHOICES[option])