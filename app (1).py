import streamlit as st

st.set_page_config(page_title="My Free Python Website", page_icon="🚀")
st.title("Welcome to My Python Website!")
st.subheader("Created using Streamlit")
st.write("This is a fully functional web application built entirely in Python. You don't need to know HTML, CSS, or JavaScript!")

name = st.text_input("What is your name?")
if name:
    st.success(f"Hello {name}! Welcome to my page.")

if st.button("Click me for a surprise"):
    st.balloons()
    st.write("🎉 You found the surprise!")
