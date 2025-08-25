import os
import re
import time
import tomllib
from datetime import datetime
from pathlib import Path
from typing import List

import github
import yaml
from loguru import logger

# Initialize GitHub connection
token = os.getenv("GITHUB_TOKEN")
gh = github.Github(token)
src_dir = Path(f"{Path(__file__).parent.parent}/src")
monarch_resource_file = Path(f"{src_dir}/data/resources.yaml")


def get_repo(repo_name: str) -> github.Repository.Repository:
    """Returns a GitHub Repository object"""
    repo = gh.get_repo(repo_name)
    return repo


def get_repos(resource_file: Path = monarch_resource_file):
    with open(resource_file, "r") as yaml_file:
        resources = yaml.safe_load(yaml_file)

    # Make dict of repositories by name
    repo_list = resources.get("repositories")

    repos = {}
    for repo in repo_list:
        repo_url = repo["id"]
        if repo_url.startswith("https://github.com/"):
            repo_id = repo_url.replace("https://github.com/", "")
            try:
                r = get_repo(repo_id)
                repos[repo_id] = r
                time.sleep(0.1)  # GitHub API rate limit is 10 requests per minute
            except Exception as e:
                logger.warning(f"{repo_url} could not be retrieved with GitHub API - {e}")
    return repos


def _get_repo_info(repo_id) -> dict:
    try:
        repo_info = get_repo(repo_id)
    except github.GithubException:
        search_rate_limit = gh.get_rate_limit().search
        wait_time = search_rate_limit.reset - datetime.utcnow()
        logger.warning(f"GitHub API rate limit exceeded - waiting {wait_time} seconds")
        time.sleep(wait_time.total_seconds() + 10)
        repo_info = get_repo(repo_id)
    return repo_info


def get_repo_file(repo: github.Repository.Repository, filepath: str) -> str | None:
    """Returns a string of the contents of a file in a GitHub Repository"""
    try:
        file_contents = repo.get_contents(filepath).decoded_content.decode("UTF-8")
    except* github.UnknownObjectException:
        logger.warning(f'Repo "{repo.name}" does not appear to have the file: {filepath}')
        file_contents = None
    return file_contents


def get_dependencies(repo: github.Repository.Repository) -> dict | None:
    """
    Returns a dictionary of the dependencies of a GitHub Repository object
    """

    def _parse_deps(deps_list: List[str]) -> dict:
        deps_dict = {}
        for dep in deps_list:
            # Split on version operators
            match = re.match(r"^([a-zA-Z0-9_-]+)\s*([><=!~]+.*)?$", dep.strip())
            if match:
                name = match.group(1)
                version = match.group(2) if match.group(2) else ""
                deps_dict[name] = version
            else:
                # Fallback for packages without version constraints
                deps_dict[dep.strip()] = ""
        return deps_dict

    try:
        project_toml = repo.get_contents("pyproject.toml").decoded_content.decode("UTF-8")
        pyproject = tomllib.loads(project_toml)
    except* github.UnknownObjectException:
        logger.warning(f'Repo "{repo.name}" does not appear to have a pyproject.toml')
        pyproject = None

    if pyproject is None:
        return None

    deps = {}
    # Check if project uses poetry or flit
    if "tool" in pyproject and "flit" in pyproject["tool"].keys():
        deplist = pyproject["tool"]["flit"]["metadata"]["requires"]
        for dep in deplist:
            d = dep.split()
            deps[d[0]] = "".join(d[1:])
    elif "tool" in pyproject and "poetry" in pyproject["tool"].keys():
        try:
            deps = pyproject["tool"]["poetry"]["dependencies"]
        except KeyError:
            # poetry also supports PEP 631 dependency specifications
            deps_list = pyproject["project"]["dependencies"]
            deps = _parse_deps(deps_list)
    else:
        try:
            deps_list = pyproject["project"]["dependencies"]
            deps = _parse_deps(deps_list)
        except KeyError:
            logger.warning(f'Could not generate dependencies for repo: "{repo.name}".')

    return deps


def get_dep_table(deps: dict, repos: dict) -> str:
    """
    Returns a markdown (str) table of repo dependencies, sorted by monarch and external
    """
    # Split into monarch and other dendencies
    monarch_deps = {}
    other_deps = {}
    for dep in deps.keys():
        if dep in repos.keys():
            monarch_deps[dep] = deps[dep]
        else:
            other_deps[dep] = deps[dep]

    # Make a markdown table of the dicts
    def row(d: dict) -> list:
        return [f"| {i} | {d[i]} |\n" for i in d]

    monarch_dep_table = (
        f"""
Monarch Dependencies

| Package | Version |
| --- | --- |
{"".join(row(monarch_deps))}"""
        if len(monarch_deps) > 0
        else ""
    )

    other_dep_table = (
        f"""
External Dependencies

| Package | Version |
| --- | --- |
{"".join(row(other_deps))}"""
        if len(other_deps) > 0
        else ""
    )

    dep_table = f"{monarch_dep_table}\n{other_dep_table}"
    return dep_table


def build_repo_page(repo: github.Repository.Repository) -> str:
    """
    Builds a markdown page (str) for a given GitHub Repository
    """
    # Initialize page contents
    page_contents = f"""
# {repo.name}

### Details

| | | 
|---|---| 
| GitHub | [{repo.full_name}]({repo.html_url}) |  
| Language | {repo.language} |  
| Description | {repo.description} |
"""

    # Get dependencies and readme
    readme = get_repo_file(repo, "README.md")
    deps = get_dependencies(repo)

    # Append dependencies and documentation, if they're not empty
    if deps:
        dep_table = get_dep_table(deps, get_repos(monarch_resource_file))
        page_contents += f"\n### Dependencies \n{dep_table}"

    if readme is not None:
        page_contents += f"\n### Documentation \n\n{readme}"
    return page_contents
