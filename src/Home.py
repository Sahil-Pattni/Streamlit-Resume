import streamlit as st
from constants import NAME, TITLE, DESCRIPTION, PRIMARY_COLOR
from components import format_page

# init()
# st.title("Sahil Pattni")

st.markdown(
    f'# Sahil Pattni\n### <div style="color: {PRIMARY_COLOR};">{TITLE}</div>',
    unsafe_allow_html=True,
)

st.markdown("#### About Me")
st.markdown(DESCRIPTION)


format_page()
