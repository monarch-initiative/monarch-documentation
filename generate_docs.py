import requests
import yaml
from github import Github

with open("resources.yaml", "r") as yaml_file:
    repositories = yaml.safe_load(yaml_file)

# TODO: Before this is ready for any serious building, or even testing, we will need to setup proper GitHub API Auth
# login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=("amc-corey-cox", "token"))

repo_responses = {}
for user, repos in repositories.get("repositories").items():
    for repo in repos:
        repo_responses[user + "/" + repo] = requests.get("https://api.github.com/repos/" + user + "/" + repo).json()

repo_info = {}
keep_keys = ["name", "full_name", "html_url", "description", "homepage", "language"]
request_keys = ["contributors", "languages", "contents", "issues", "labels", "releases", "deployments"]
for repo, response in repo_responses.items():
    repo_info[repo] = {key: value for key, value in response.items() if key in keep_keys}
    for key in request_keys:
        repo_info[repo][key] = requests.get(repo_responses[repo][key + "_url"]).json()
