import streamlit as st

st.header("Contact Us")

with st.form(key="myForm"):
    user_email = st.text_input("Your Email Address")
    your_message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)