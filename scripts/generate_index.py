import os
from pathlib import Path

from loguru import logger
import yaml

from utils import get_repo, get_repos


logger.info("Generating index page...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs")
src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")

repos = get_repos(resource_file)

repos_table = "| Repository | Description |\n| | |\n"
for name, repo in repos.items():
    repos_table += f"| [{name}](./Repositories/{name}) | {repo.description} |\n"

page_contents = f"""
## Monarch Technical Documentation

The Monarch Initiative Knowledge Graph (Monarch KG) is created using a constellation of tools and packages created by the Monarch Initiative team and our collaborators.  
Here you can find information about the connections between the Monarch Intiative tools and how they are used to create the Monarch Graph.  

## Monarch Software Infrastructure

(Insert a description of the various "sub-workflows" within the overall Monarch pipeline)

(Placeholder image)
<img src='images/docs-coming-soon.jpg' width=420, style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>

### Repositories
{repos_table}

"""

with open(f"{docs_dir}/index.md", "w") as outfile:
    outfile.write(page_contents)
