# Streamlit Personal Website Template
This is a minimalistic template for creating your own personal website using [Streamlit](https://streamlit.io/). No other dependencies are needed. You can see a demo of the template [here (not yet deployed)]().

## How to Use
The content is managed via the YAML files in the `resources` directory. Replace these with your own content, and add/remove YAML files as needed. The YAML files are read in and rendered in order of their `rank` attribute.

You'll find several themes in the `config.toml` file. You can switch themes by keeping the one you want uncommented.

Currently, my name and the home page are hardcoded. I'll be changing this so it can be modified via a YAML file.