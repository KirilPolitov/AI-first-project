import streamlit as st
st.title("Nut GPT")
name = st.text_input("Enter Prompt")
if name:
  st.write(f"{name}")
