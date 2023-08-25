from components import format_page, header, project_card
import math
import yaml
import os

format_page()

header("Projects")

# Parse project details from YAML files
projects = []
for filename in os.listdir("resources/projects"):
    if filename.endswith(".yaml"):
        with open(f"resources/projects/{filename}") as f:
            details = yaml.load(f, Loader=yaml.FullLoader)
            if "url" not in details:
                details["url"] = None
            if "rank" not in details:
                details["rank"] = math.inf
            projects.append(details)


# Sort projects by rank (ascending)
projects.sort(key=lambda x: x["rank"])

# Generate project cards
for project in projects:
    project_card(
        project["title"],
        project["tools"],
        project["description"],
        project["url"],
    )
