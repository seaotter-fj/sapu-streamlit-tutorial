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
st.image(
    "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg", 
    width=400)