import streamlit as st
from constants import NAME, TITLE, DESCRIPTION, PRIMARY_COLOR, init
from components import format_page

init()

st.markdown(
    f'# {NAME}\n### <div style="color: {PRIMARY_COLOR};">{TITLE}</div>',
    unsafe_allow_html=True,
)

st.markdown("#### About Me")
st.markdown(DESCRIPTION)


format_page()
