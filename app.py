import streamlit as st
st.title("sybau")
name = st.text_input("mi bomboclat")
if name:
  st.write(f"{name}")
