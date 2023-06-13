from pathlib import Path

from loguru import logger

from utils import get_repo, get_repo_file


logger.info("Generating Ingest Principles page...")

# Get resource files and set paths
docs_dir = Path(f"{Path(__file__).parent.parent}/docs") 
src_dir = Path(f"{Path(__file__).parent.parent}/src")
out_dir = Path(f"{docs_dir}/Ingest Principles")

monarch_ingest = get_repo("monarch-initiative/monarch-ingest")
modeling_principles = get_repo_file(monarch_ingest, "docs/Principles/modeling-principles.md")
# mapping_principles = get_repo_file("docs/Principles/mapping-principles.md", "README.md")

page_contents = f"""
# Ingest Principles

## Overview

The Monarch Knowledge Graph (KG) is built from a variety of data sources in the biomedical domain.  
These data sources are "ingested" into the KG using a variety of tools and packages created by the Monarch Initiative team and our collaborators.  
This page describes the principles that guide the ingestion process.  

## General Principles

1. All ingests should have a stringent (defensive) filtering strategy.  

1. Utilize Biolink profiles to inform the filtering of incoming ingests (ex. Phenio)  

1. Use yaml to implement this  

1.  All nodes should have a category attached.

"""

out_dir.mkdir(parents=True, exist_ok=True)
with open(f"{out_dir}/index.md", "w") as outfile:
        outfile.write(page_contents)

with open(f"{out_dir}/modeling-principles.md", "w") as outfile:
        outfile.write(modeling_principles)

# with open(f"{out_dir}/mapping-principles.md", "w") as outfile:
#         outfile.write(mapping_principles)