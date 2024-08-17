import streamlit as st
import pandas as pd


st.set_page_config(layout='wide', page_title='Home')

col1, col2 = st.columns(2)

col3, inter_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('data.csv', sep=';')
count_row = df.shape[0]

with col1:
    st.image('images/photo.jpg',)

with col2:
    st.title('Gleb Ponasenkov')
    st.write(
        "I'm Gleb, a beginner Python developer passionate about creating apps that solve problems and make life easier. "
        "On this site, you'll find a collection of my projects, each reflecting my journey as I learn and grow in the "
        "world of programming. Whether it's simple tools or more complex applications, I'm excited to share my work "
        "with you and showcase what I've been learning along the way.")

with col3:
    for index in range(count_row):
        if index % 2 == 0:
            st.header(df.iloc[index]['title'])
            st.write(df.iloc[index]['description'])
            st.image('images/' + df.iloc[index]['image'])
            st.link_button(label='Source code', url=df.iloc[index]['url'], use_container_width=True)
with col4:
    for index in range(count_row):
        if index % 2 != 0:
            st.header(df.iloc[index]['title'])
            st.write(df.iloc[index]['description'])
            st.image('images/' + df.iloc[index]['image'])
            st.link_button(label='Source code', url=df.iloc[index]['url'], use_container_width=True)
