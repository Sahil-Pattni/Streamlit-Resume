import toml
import yaml

# Global variables
(
    COLOR_SCHEME,
    PRIMARY_COLOR,
    BACKGROUND_COLOR,
    SECONDARY_BACKGROUND_COLOR,
    TEXT_COLOR,
) = (
    None,
    None,
    None,
    None,
    None,
)

NAME, TITLE, DESCRIPTION = None, None, None

# Socials
SOCIALS = None


def init():
    global COLOR_SCHEME, PRIMARY_COLOR, BACKGROUND_COLOR, SECONDARY_BACKGROUND_COLOR, TEXT_COLOR
    global NAME, TITLE, DESCRIPTION, SOCIALS

    # Get color cheme
    COLOR_SCHEME = toml.load(".streamlit/config.toml")
    PRIMARY_COLOR = COLOR_SCHEME["theme"]["primaryColor"]
    BACKGROUND_COLOR = COLOR_SCHEME["theme"]["backgroundColor"]
    SECONDARY_BACKGROUND_COLOR = COLOR_SCHEME["theme"]["secondaryBackgroundColor"]
    TEXT_COLOR = COLOR_SCHEME["theme"]["textColor"]

    # Load personal information
    try:
        with open("resources/personal.yaml") as f:
            info = yaml.load(f, Loader=yaml.FullLoader)
            NAME, TITLE, DESCRIPTION = info["name"], info["title"], info["description"]
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
