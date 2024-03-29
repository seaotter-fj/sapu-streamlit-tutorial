import streamlit as st 
from PIL import Image
import datetime
from typing import List
import pandas as pd
import matplotlib.pyplot as plt

# form_btn が押されるまではリロードされません。
with st.form(key='profile_form'):
    # textbox
    name = st.text_input('Name')
    address = st.text_input('Address')

    # single select
    age_category: str = st.radio(
        '年齢層',
        ('子供（18歳未満）', '大人（over 18）') # 選択肢は tuppl で。
    )
    
    # multi select
    hobby: List[str] = st.multiselect(
        '趣味',
        ('sports', 'reading books', 'programming', 'anime/movie', 'fishing', 'cokking')
    )
    
    # slider 
    height = st.slider('height', min_value=110, max_value=240)
    
    # date 
    start_date = st.date_input(
        'start day',
        datetime.date(2023, 4, 4)
    )
    
    # button
    submit_btn = st.form_submit_button('submit')
    cancel_btn = st.form_submit_button('cancel')

    if submit_btn:
        st.text(f'ようこそ！{age_category}, {name}さん🎵 {address}に送っといたよ。')
        st.text(f'趣味: {", ".join(hobby)}')