from pathlib import Path
from utils import get_repos, build_repo_page
from log import get_logger

log = get_logger(__name__)

log.info("Generating repository pages...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs") 
src_dir = Path(f"{Path(__file__).parent.parent}/src")
resource_file = Path(f"{src_dir}/data/resources.yaml")

repos = get_repos(resource_file)

# Generate a markdown page for each repo
for repo_name in repos:
    log.info(f"Generating page for {repo_name}...")
    repo = repos[repo_name]
    
    page_contents = build_repo_page(repo)

    Path(f"{docs_dir}/Repositories").mkdir(parents=True, exist_ok=True)
    with open(f"{docs_dir}/Repositories/{repo.name}.md", "w") as outfile:
            outfile.write(page_contents)
