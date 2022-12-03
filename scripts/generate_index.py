import os
from pathlib import Path
import github
import yaml
from utils import get_repos
from log import get_logger
log = get_logger(__name__)

log.info("Generating index page...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs") 
src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")

repos = get_repos(resource_file)

token = os.getenv('GITHUB_TOKEN')
g = github.Github(token)

with open(resource_file, "r") as yaml_file:
    resources = yaml.safe_load(yaml_file)

repo_reference = resources.get("repositories")
repos = {}
for repo in repo_reference:
    repo_url = repo['id']
    if repo_url.startswith("https://github.com/"):
        repo_id = repo_url.replace("https://github.com/","")
        r = g.get_repo(repo_id)
        repos[repo_id] = r

repos_str = ""
for repo_name in repos.keys():
    repo = repos[repo_name]
    repos_str += f"""
- [{repo.name}](./Repositories/{repo.name}) - {repo.description}  
"""

page_contents = f"""
## Monarch Technical Documentation

The Monarch Initiative Knowledge Graph (Monarch KG) is created using a constellation of tools and packages created by the Monarch Initiative team and our collaborators.  
Here you can find information about the connections between the Monarch Intiative tools and how they are used to create the Monarch Graph.  

## Monarch Software Infrastructure

(Insert a description of the various "sub-workflows" within the overall Monarch pipeline)

(Placeholder image)
<img src='images/docs-coming-soon.jpg' width=420, style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>

### Repositories
{repos_str}

"""

with open(f"{docs_dir}/index.md", "w") as outfile:
    outfile.write(page_contents)
