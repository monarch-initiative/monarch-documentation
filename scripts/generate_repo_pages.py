from pathlib import Path

from loguru import logger

from utils import get_repos, build_repo_page


logger.info("Generating repository pages...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs") 
src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")
out_dir = Path(f"{docs_dir}/Repositories")

repos = get_repos(resource_file)

# Generate a markdown page for each repo
for repo_name in repos:
    logger.info(f"Generating page for {repo_name}...")
    repo = repos[repo_name]
    
    page_contents = build_repo_page(repo)

    out_dir.mkdir(parents=True, exist_ok=True)
    with open(f"{out_dir}/{repo.name}.md", "w") as outfile:
            outfile.write(page_contents)
