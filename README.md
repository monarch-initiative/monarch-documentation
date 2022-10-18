# Monarch Technical Documentation

Technical documentation for all Monarch applications, packages, services and related projects.

[See the docs here](https://monarch-initiative.github.io/monarch-technical-documentation)

## Overview
The Monarch Initiative Knowledge Graph (Monarch KG) is created using a constellation of tools and packages created by the Monarch Initiative team and our collaboratores.  
This repository exists to document the connections between the Monarch Intiative tools and how they are used to create the Monarch Graph.  
The intent of this repository is to serve as the source of truth for documentation of the project overall, containing information and documentation for each repository,  
as well as documentation for how the different software tools are used together.

## Contents
This repository will host the higher-order structure documentation of the Monarch Intiative Knowledge Graph Tools and as a build platform for integrating all of the documentation of each of requisite resources used to construct the Monarch Intiative Knowledge Graph and make it useable to others. This project consists of the following tools to build and deploy the Monarch Initiative Technical Documentation.

- [Markdown Generation Scripts](scripts/) - Python scripts to pull documentation from resources to aggregate in Monarch Technical Documentation pages.
- [src/](src/) - Source files for LinkML Cookie Cutter
    - [monarch_technical_documentation/](src/monarch_technical_documentation)
        - [Monarch Technical Documentation LinkML Schema](src/monarch_technical_documentation/schema/monarch_technical_documentation.yaml) - Describes the Schema for the Monarch Technical Documentation
        - [Monarch Resources Yaml](src/data/resources.yaml) - LinkML-schema YAML file detailing the various Monarhc resources, and repositories for each software resource.
- [project/](project/) - project files (do not edit these)

## Developer Documentation

Use the `make` command to generate project artifacts:
- `make all`: make everything
- `make deploy`: deploys site

## Credits

This project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)