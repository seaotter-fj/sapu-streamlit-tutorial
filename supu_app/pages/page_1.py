import streamlit as st 
from PIL import Image
import datetime
from typing import List
import pandas as pd
import matplotlib.pyplot as plt

code = '''
    import streamlit as st
    st.title('Sapu app')
    # こんな感じで書いていくよ。
    '''

st.code(code, language='python')