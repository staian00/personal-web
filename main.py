import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Home')

col1, inter_col, col2 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('data.csv', sep=';')
count_row = df.shape[0]

with col1:
    for index in range(count_row):
        if index % 2 == 0:
            st.header(df.iloc[index]['title'])
            st.write(df.iloc[index]['description'])
            st.image('images/' + df.iloc[index]['image'])
            st.link_button(label='Source code', url=df.iloc[index]['url'], use_container_width=True)
with col2:
    for index in range(count_row):
        if index % 2 != 0:
            st.header(df.iloc[index]['title'])
            st.write(df.iloc[index]['description'])
            st.image('images/' + df.iloc[index]['image'])
            st.link_button(label='Source code', url=df.iloc[index]['url'], use_container_width=True)
