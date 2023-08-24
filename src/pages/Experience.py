from components import format_page, header, experience_card
import math
import yaml
import os

header("Experience")

# Parse experience details from YAML files
experiences = []
for filename in os.listdir("resources/experience"):
    if filename.endswith(".yaml"):
        with open(f"resources/experience/{filename}") as f:
            details = yaml.load(f, Loader=yaml.FullLoader)
            if "rank" not in details:
                details["rank"] = math.inf
            experiences.append(details)

# Sort experiences by rank (ascending)
experiences.sort(key=lambda x: x["rank"])

# Generate experience cards
for experience in experiences:
    experience_card(
        experience["title"],
        experience["company"],
        experience["duration"],
        experience["location"],
        experience["description"],
    )


format_page()
