import toml
import yaml

# Global variables
THEME = None
INFO = None
SOCIALS = None


def init():
    global THEME, INFO, SOCIALS

    # Get color cheme
    THEME = toml.load(".streamlit/config.toml")["theme"]

    # Load personal information
    try:
        with open("resources/personal.yaml") as f:
            INFO = yaml.load(f, Loader=yaml.FullLoader)
    except:
        print("Error: Could not load personal information.")
        exit(1)

    # Load socials
    try:
        with open("resources/socials.yaml") as f:
            SOCIALS = yaml.load(f, Loader=yaml.FullLoader)
    except:
        print("Error: Could not load socials.")


init()
