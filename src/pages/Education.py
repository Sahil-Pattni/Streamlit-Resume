from components import format_page, header, education_card
import math
import yaml
import os

format_page()
header("Education")

# Parse education details from YAML files
universities = []
for filename in os.listdir("resources/education"):
    if filename.endswith("yaml"):
        with open(f"resources/education/{filename}") as f:
            details = yaml.load(f, Loader=yaml.FullLoader)
            if "rank" not in details:
                details["rank"] = math.inf
            universities.append(details)

# Sort universities by rank (ascending)
universities.sort(key=lambda x: x["rank"])

# Generate education cards
for university in universities:
    education_card(
        university["institution"],
        university["program"],
        university["duration"],
        university["location"],
        university["description"],
    )
