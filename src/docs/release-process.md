# Monarch Release Process

## Overview

This document describes the steps required to create a new Monarch release.  

These releases consist primarily of the following components:  

- Monarch Mapping files via [Monarch Mapping Commons](https://github.com/monarch-initiative/monarch-mapping-commons)
- Knowledge Graph via [Monarch Ingest](https://github.com/monarch-initiative/monarch-ingest)
- Data library and API via [Monarch-Py](https://github.com/monarch-initiative/monarch-app/backend)
- Monarch website via [Monarch-App](https://github.com/monarch-initiative/monarch-app/frontend)


## Monarch Mapping Commons

TBD

## Monarch Ingest (Knowledge Graph)

Monarch's knowledge graph is built using the Monarch Ingest pipeline. 
The pipeline is run on a Jenkins server, and the resulting knowledge graph is uploaded to both Monarch's data bucket on Google Cloud, as well as the KG-Hub AWS S3 bucket.

Changes to the Monarch Ingest pipeline are made in the [Monarch Ingest](https://github.com/monarch-initiative/monarch-ingest) repository.

After the knowledge graph has been built, the [QC Dashboard](https://github.com/monarch-initiative/monarch-qc) is used to verify the quality of the knowledge graph.

Once the knowledge graph has been verified, additional steps are required to make the new knowledge graph available to the dev, beta, and production versions of the Monarch website.

### Deploying the Knowledge Graph

#### Deploying to dev

While the Github Actions workflow for Monarch App will automatically update and deploy the dev environment, there may be times when the knowledge graph is updated without a corresponding update to the Monarch App code. In these cases, the knowledge graph must be manually deployed to the dev environment.

To deploy the knowledge graph to the dev environment, follow these steps:

#### Deploying to beta

Then make an env in v3 stack, bring it up, and connect it to beta in the load balancer  
Then, uh, confirm that it works? get other people to thumbs up?

#### Deploying to production

Then switch the load balancer to pointing to it as production  
Then turn off the former production  
And source the former former env in v3 stack to delete it

## Monarch-Py (Monarch-App backend)

TBD

## Monarch Website (Monarch-App frontend)

TBD
