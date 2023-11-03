from pathlib import Path

from loguru import logger
import yaml


logger.info("Generating index page...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs")
src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")

with open(resource_file, "r") as yaml_file:
    resources = yaml.safe_load(yaml_file)

repo_reference = resources.get("documentations")
docs_table = ""

for repo in repo_reference:
    doc_url = repo['id']
    doc_name = repo['name']
    doc_description = repo['description'] if 'description' in repo else ""
    doc_repository = repo['repository'] if 'repository' in repo else "https://github.com/monarch-initiative/helpdesk/issues"
    row = "| " + f"[{doc_name}]({doc_url})" + " | "+ doc_description + " | "+ f"[Issue Tracker]({doc_repository}/issues)" + " |\n"
    docs_table += row

page_contents = f"""
## Monarch Documentation

The Monarch Initiative and our collaborators develop a wide range of tools and ontologies to tackle global challenges such as Rare Disease.
Here we document the software and data infrastructure across the entire Monarch ecosystem. If you would like any specific documentation to be added
please use [our Monarch-wide issue tracker](https://github.com/monarch-initiative/helpdesk/issues).

### Important documentation across the Monarch Initiative ecosystem

| Repository | Description | Tracker |
| --- | --- | --- |
{docs_table}

"""

with open(f"{docs_dir}/index.md", "w") as outfile:
    outfile.write(page_contents)
