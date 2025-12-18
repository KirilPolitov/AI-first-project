import streamlit as st
st.title("Crab GPT")
name = st.text_input("Enter Prompt")
if name:
  st.write(f"{name}")
