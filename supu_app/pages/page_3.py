import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open(r'./data/data.csv') as csv_file:
    df = pd.read_csv(csv_file)
    df.columns = ['one', 'two', 'three']
    
st.dataframe(df)
fig, ax = plt.subplots()
ax.scatter(df['one'], df['two'])
st.pyplot(fig)