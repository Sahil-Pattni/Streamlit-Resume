# Streamlit Personal Website Template

![screenshot](resources/images/retro_screenshot.png)

<div style="display: flex; justify-content: space-between;">
    <img src="resources/images/bright_screenshot.png" alt="Slate Screenshot" width="49.5%">
    <img src="resources/images/slate_screenshot.png" alt="Minimal Screenshot" width="49.5%">
</div>
<br>

![screenshot](resources/images/minimal_screenshot.png)



This is a minimalistic template for creating your own personal website using [Streamlit](https://streamlit.io/). No other dependencies are needed. You can see a live demo of the template [here](https://sahilpattni.streamlit.app).

## How to Use
The content is managed via the YAML files in the `resources` directory. Replace these with your own content, and add/remove YAML files as needed. 
The YAML files in each section are read in and rendered in order of their `rank` attribute.

You'll find several themes in the `config.toml` file. You can switch themes by keeping the one you want uncommented.