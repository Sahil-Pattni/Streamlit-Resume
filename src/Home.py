import streamlit as st
from constants import init, THEME, INFO
from components import format_page

format_page()
init()

st.markdown(
    f'# {INFO["name"]}\n### <div style="color: {THEME["primaryColor"]};">{INFO["title"]}</div>',
    unsafe_allow_html=True,
)

st.markdown("#### About Me")
st.markdown(INFO["description"])

st.divider()

c1, c2, c3 = st.columns([1, 1, 1])

with c1:
    for number in INFO["numbers"]:
        st.markdown(
            f"###### <div style='text-align: left;'>{number}</div>",
            unsafe_allow_html=True,
        )

with c2:
    st.markdown(
        f"###### <div style='text-align: center;'>{INFO['email']}</div>",
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"###### <div style='text-align: right;'>{INFO['location']}</div>",
        unsafe_allow_html=True,
    )
