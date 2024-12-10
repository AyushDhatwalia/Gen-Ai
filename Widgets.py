import streamlit as st
st.title("streamlit Text Input")
name=st.text_input("Enter your Name")
if name:
    st.write(f"Hello, {name}")