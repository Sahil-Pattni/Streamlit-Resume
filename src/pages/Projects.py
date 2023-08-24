import streamlit as st
from components import header, project_card
import os
import yaml

header("Projects")

for filename in os.listdir("resources/projects"):
    if filename.endswith(".yaml"):
        with open(f"resources/projects/{filename}") as f:
            details = yaml.load(f, Loader=yaml.FullLoader)
            url = details["url"] if "url" in details else None
            project_card(
                details["title"], details["tools"], details["description"], url
            )
