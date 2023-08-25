import streamlit as st
from constants import *

init()


def header(section: str, name: str = "Sahil Pattni") -> None:
    """
    Generates the header of the website.

    Args:
        section (str): The section to be displayed in the header.
        name (str, optional): The name to be displayed in the header. Defaults to "Sahil Pattni".
    """
    st.set_page_config(
        page_title="Sahil Pattni",
    )
    st.title(name)
    st.markdown(f"## {section}")

    # Spacer
    st.markdown(
        """

            """
    )


def project_card(title: str, tools: str, description: str, url: str = None) -> None:
    """
    Generates a project card.

    Args:
        title (str): The title of the project.
        tools (str): The tools, frameworks and languages used in the project.
        description (str): The description of the project. Accepts markdown syntax.
        url (str, optional): The URL of the project. Defaults to None.
    """

    # Add link to project
    if url:
        description += f"\n\n[View Project]({url})"
    st.markdown(
        f'### <div style="text-align: left; color: {PRIMARY_COLOR};">{title}</div>',
        unsafe_allow_html=True,
    )

    # Tools
    st.markdown(
        f'##### <div style="text-align: left;">{tools}</div>',
        unsafe_allow_html=True,
    )

    # DESCRIPTION
    st.markdown(description)

    st.divider()


def education_card(
    institution: str, program: str, duration: str, location: str, description: str
) -> None:
    """
    Generates an education card.

    Args:
        institution (str): The name of the institution.
        program (str): The program of study.
        duration (str): The duration of the program.
        description (str): The description of the program. Accepts markdown syntax.
    """
    st.markdown(
        f'### <div style="color: {COLOR_SCHEME["theme"]["primaryColor"]};">{institution}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"##### {program}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'###### <div style="text-align: left;">{location}</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'###### <div style="text-align: right;">{duration}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(description)

    st.divider()


def experience_card(
    title: str, company: str, duration: str, location: str, description: str
) -> None:
    """
    Generates an experience card.

    Args:
        title (str): The title of the experience.
        company (str): The company of the experience.
        duration (str): The duration of the experience.
        description (str): The description of the experience. Accepts markdown syntax.
    """
    st.markdown(
        f'### <div style="color: {COLOR_SCHEME["theme"]["primaryColor"]};">{title}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(f"##### {company}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'###### <div style="text-align: left;">{location}</div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'###### <div style="text-align: right;">{duration}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(description)

    st.divider()


def format_page():
    """
    Applies custom styling to the page, and adds a copyright notice on
    the sidebar and footer.
    """

    st.markdown(
        "<style>a:link, a:visited, a:hover, a:active { color: "
        + COLOR_SCHEME["theme"]["primaryColor"]
        + ";}</style>",
        unsafe_allow_html=True,
    )

    if "headerColor" not in COLOR_SCHEME["theme"]:
        COLOR_SCHEME["theme"]["headerColor"] = COLOR_SCHEME["theme"]["textColor"]

    st.markdown(
        "<style> h1 {color: " + COLOR_SCHEME["theme"]["headerColor"] + ";} </style>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
        footer {visibility: hidden;}

        footer:hover,  footer:active {
            color: #ffffff;
            background-color: transparent;
            text-decoration: underline;
            transition: 400ms ease 0s;
        }

        footer:after {
            content:'© 2023 Sahil Pattni. All rights reserved.'; 
            visibility: visible;
            display: block;
            position: relative;
            padding: 5px;
            top: 2px;
        }

        a:link, a:visited, a:hover, a:active {
                text-decoration: none;
        }
        
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Socials

    st.sidebar.markdown(
        f"""
        ####
        #### <a href='{SOCIALS['linkedin']}' target='_blank'>LinkedIn</a><br>
        #### <a href='{SOCIALS['github']}' target='_blank'>GitHub</a><br>
        #### <a href='{SOCIALS['email']}' target='_blank'>Email</a><br>
        """,
        unsafe_allow_html=True,
    )

    # Copyright
    st.sidebar.caption("© 2023 Sahil Pattni. All rights reserved.")
