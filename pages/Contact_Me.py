import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='mail_form', clear_on_submit=True):
    user_email = st.text_input('Your email address')
    message = st.text_area('Your message')
    button = st.form_submit_button('Submit')
    if button:
        send_email(sender=user_email, text=message)
        st.info('Your message was sent successfully')
