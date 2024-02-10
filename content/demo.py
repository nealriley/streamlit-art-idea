import numpy as np
import pandas as pd
import time
import streamlit as st

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

def stream_data():
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.06)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.08)

def stream_words():
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.06)