import streamlit as st


def header(section: str, name: str = "Sahil Pattni") -> None:
    """
    Generates the header of the website.

    Args:
        section (str): The section to be displayed in the header.
        name (str, optional): The name to be displayed in the header. Defaults to "Sahil Pattni".
    """
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
    col1, col2 = st.columns(2)

    # TITLE
    with col1:
        title = f"[{title}]({url})" if url else title
        st.markdown(
            f'### <div style="text-align: left;">{title}</div>',
            unsafe_allow_html=True,
        )

    # TOOLS
    with col2:
        st.markdown(
            f'#### <div style="text-align: right;">{tools}</div>',
            unsafe_allow_html=True,
        )

    # DESCRIPTION
    st.markdown(description)

    st.divider()
