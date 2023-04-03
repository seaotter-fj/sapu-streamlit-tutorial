import streamlit as st 
from PIL import Image
import datetime
from typing import List
import pandas as pd
import matplotlib.pyplot as plt

st.title('さぷーアプリ')
st.caption('This is a test app in the sapu tutorial.')

# image = Image.open('./data/download.jpg')
# image = Image.open('../supu_app/data/download.jpg')
image = Image.open(r'./sticker_3.png')
st.image(image, width=200)