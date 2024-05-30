import streamlit as st
import send_email
import pandas as pd

df = pd.read_csv('files/topics.csv')

st.header('Contact Me')





with st.form(key='email_form'):
    user_email = st.text_input("Your Email Address")

    user_selection = st.selectbox('What topic do you want to discuss?', df['topic'])
    init_message = st.text_area("Your Message")
    message = f"""\
Subject: New Email from {user_email}
From: {user_email}
Topic {user_selection}
{init_message}
"""

    button = st.form_submit_button('Submit')
    if button:
        send_email.sendemail(message, user_email)
        st.info("Your email was sent successfully")
