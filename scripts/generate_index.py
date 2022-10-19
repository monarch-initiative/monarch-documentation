import requests
import yaml
import os
from pathlib import Path
from github import Github

### TODO:
# - For files, we should pull in the download.yaml from each repository using the contents_url key from the response.
# - Before this is ready for any serious building, or even testing, we will need to setup proper GitHub API Auth

src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")

with open(resource_file, "r") as yaml_file:
    resources = yaml.safe_load(yaml_file)

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

repo_reference = resources.get("repositories")
repos = {}
for user in repo_reference.keys():
    for repo in repo_reference.get(user):
        r = g.get_repo(f"{user}/{repo}")
        repos[f"{user}/{repo}"] = r

repo_info = {}
for repo_name, repo in repos.items():
    repo_info[repo.full_name] = {
        "name": repo.name,
        "full_name": repo.full_name,
        "html_url": repo.html_url,
        "description": repo.description if repo.description is not None else "No description found",
        "homepage": repo.homepage,
        "language": repo.language,
        "contributors_url": repo.contributors_url,
        "languages_url": repo.languages_url,
        "contents_url": repo.contents_url,
        "issues_url": repo.issues_url,
        "labels_url": repo.labels_url,
        "releases_url": repo.releases_url,
        "deployments_url": repo.deployments_url
    }

repo_list = ""
for repo_name in repo_info:
    repo = repo_info[repo_name]
    repo_list += f"""
- [{repo['name']}]({repo['html_url']}) - {repo['description']}  
"""

page_contents = f"""# Monarch Initiative - Technical Documentation

**Welcome to the Monarch Initiative Technical Documentation!**  

The Monarch Initiative Knowledge Graph (Monarch KG) is created using a constellation of tools and packages created by the Monarch Initiative team and our collaborators.  
Here you can find information about the connections between the Monarch Intiative tools and how they are used to create the Monarch Graph.  

## Monarch Software Infrastructure

(Insert a description of the various "sub-workflows" within the overall Monarch pipeline)

(Placeholder image)
<img src='images/docs-coming-soon.jpg' width=420, style='display: block; margin-left: auto; margin-right: auto; width: 60%;'>

### Repositories
{repo_list}

"""

with open('docs/index.md', 'w') as outfile:
    outfile.write(page_contents)