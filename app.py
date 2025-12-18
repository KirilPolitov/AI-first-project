import streamlit as st
st.title("Crap GPT")
name = st.text_input("Enter Prompt")
if name:
  st.write(f"{name}")
