import streamlit as st
import streamlit as st
from PIL import Image


image = Image.open("resources/images/transparent.png")

col1, col2 = st.columns(2)

with col2:
    # Add image to sidebar
    st.image(image, width=300)

with col1:
    st.title("Sahil Pattni")
    st.subheader("Software Developer")
st.markdown(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis venenatis lectus et felis elementum porta. Phasellus vitae malesuada ex. Nullam sodales, dolor dapibus tincidunt imperdiet, odio enim varius nibh, vel viverra nisl odio vitae dui. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus eget convallis purus, ac consectetur metus. In hac habitasse platea dictumst. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
    Nunc consectetur egestas maximus. Integer ornare pharetra maximus. Suspendisse ac eros eu lorem bibendum gravida. Sed a mattis mi. Ut aliquet lorem sapien, sed consequat urna interdum eu. Donec vel sapien lacus. Vivamus urna lectus, accumsan vel facilisis ac, consectetur vel odio. Vestibulum rhoncus porta felis, non congue lacus placerat et. Pellentesque rutrum turpis justo, id rhoncus orci bibendum vitae. Etiam mattis velit mauris, id malesuada mi fermentum at. Curabitur ex ligula, consequat in nulla eget, posuere dapibus metus.
    """
)
