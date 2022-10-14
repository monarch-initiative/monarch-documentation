import requests
import yaml
from github import Github

with open("resources.yaml", "r") as yaml_file:
    resources = yaml.safe_load(yaml_file)


# TODO: Before this is ready for any serious building, or even testing, we will need to setup proper GitHub API Auth
# login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=("amc-corey-cox", "token"))
auth_token = "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"
auth_header = {"Authorization": "Bearer " + auth_token}
# login = requests.get('https://api.github.com/search/repositories?q=github+api', headers=auth_header)

repositories = resources.get("repositories")
repo_responses = {}
for user in repositories.keys():
    for repo in repositories.get(user):
        full_repo_name = user + "/" + repo
        request_url = "https://api.github.com/repos/" + full_repo_name
        repo_responses[full_repo_name] = requests.get(request_url, headers=auth_header).json()

repo_info = {}
keep_keys = ["name", "full_name", "html_url", "description", "homepage", "language"]
request_keys = ["contributors", "languages", "contents", "issues", "labels", "releases", "deployments"]
for repo, response in repo_responses.items():
    repo_info[repo] = {key: value for key, value in response.items() if key in keep_keys}
    for key in request_keys:
        repo_info[repo][key] = requests.get(repo_responses[repo][key + "_url"]).json()

with open('docs/index.md', 'w') as outfile:
    yaml.dump(repo_info, outfile, default_flow_style=False)

# for files, we should pull in the download.yaml from each repository using the contents_url key from the response.
