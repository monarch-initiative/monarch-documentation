# Monarch Release Process

## Overview

This document describes the steps required to create a new Monarch release.  

These releases consist primarily of the following components:  

- Monarch Mapping files via [Monarch Mapping Commons](https://github.com/monarch-initiative/monarch-mapping-commons)
- Knowledge Graph via [Monarch Ingest](https://github.com/monarch-initiative/monarch-ingest)
- Data library and API via [Monarch-Py](https://github.com/monarch-initiative/monarch-app/backend)
- Monarch website via [Monarch-App](https://github.com/monarch-initiative/monarch-app/frontend)


## Monarch Mapping Commons

[Monarch Mapping Commons](https://github.com/monarch-initiative/monarch-mapping-commons) is a repository repository contains code used to generate the mapping files used in the creation of the Monarch knowledge graph.  
The nodes and edges in the knowledge graph come from a variety of sources, and have varying IDs and prefixes.  
The mapping files are used to map these IDs to IDs in Monarch's preferred namespaces.

These mapping files are generated via a Jenkins job on a weekly basis, and are stored in the [Monarch Data Bucket](https://data.monarchinitiative.org/mappings/index.html).

## Monarch Ingest (Knowledge Graph)

Monarch's knowledge graph is built using the Monarch Ingest pipeline. 
The pipeline is run on a Jenkins server, and the resulting knowledge graph is uploaded to both Monarch's data bucket on Google Cloud, as well as the KG-Hub AWS S3 bucket.

Changes to the Monarch Ingest pipeline are made in the [Monarch Ingest](https://github.com/monarch-initiative/monarch-ingest) repository.

After the knowledge graph has been built, the [QC Dashboard](https://github.com/monarch-initiative/monarch-qc) is used to verify the difference between the new build of the knowledge graph and the previous build.

Once the knowledge graph has been verified, additional steps are required to make the new knowledge graph available to the dev, beta, and production versions of the Monarch website.

### Deploying the Knowledge Graph

#### Deploying to dev

While the Github Actions workflow for Monarch App will automatically update and deploy API & UI code to the dev environment, the knowledge graph must be manually deployed to the dev environment.

To deploy the knowledge graph to the dev environment, follow these steps:

* Checkout (or update) [Monarch Stack V3](https://github.com/monarch-initiative/monarch-stack-v3)
* Source the dev environment: `cd deployment && source site-envs/monarch-dev.env`
* Run the provision script to update the dev environment: `./provision.sh`
* After running the provision script to update the dev environment, a manual restart of the Solr container is necessary:

```
gcloud compute ssh --zone us-central1-a monarch-v3-${TF_VAR_env}-manager -- sudo docker service update --force monarch-v3_solr
```

From this point forward, code updates on the dev environment will be automatically deployed and additional work will happen to finish the work planned for the milestone. Ideally changes to the graph will happen early in the release cycle.

#### Deploying to beta

Once work on the milestone is complete, the release can be tagged and deployed to the beta environment. 
Copy the latest release env file to a new env, for example: `cp site-envs/monarch-2023-10-11.env site-envs/monarch-2023-11-16.env` 
The date for the environment file name should match the KG release version, rather than today's date. 
Edit the top two lines in new env to match the latest KG & API versions:

```
export MONARCH_KG_VERSION="2023-11-16"
export MONARCH_API_VERSION="0.18.1"
```

Then source the new environment and run provision.sh to create the new VM stack, paying attention to the terrform output to make sure that it's creating VMs with a version name you expect:

```
source site-envs/monarch-2023-11-16.env
./provision.sh
```
#### Connecting beta to the load balancer

Once this completes, open the [GCP load balancer configuration](https://console.cloud.google.com/net-services/loadbalancing/details/http/monarch-balancer?project=monarch-initiative). 

1. Click on the **edit** link at the top of the page.
2. Click on **Backend Configuration**
3. Open the **Backend services & backend buckets** pull down on the right side and check `monarch-v3-{release}-api-backend` & `monarch-v3-{release}-nginx-backend`
4. Open the `Host and path rules` section to point beta.monarchinitiative.org to the nginx backend and api-beta.monarchinitiative.org to the api backend,  

Restart the load balancer with the new configuration and confirm that the site is up and running. 

Get yourself a cup of hot chocolate / ice cold lemonade (season dependent) and settle in to go through the issues in the milestone. Make sure that each issue appears to actually be fixed, and close them with a note that they're confirmed to be working on beta.monarchinitiative.org. (with some additional explanation for externally submitted issues about when the change is expected to be visible on the production site)


#### Deploying to production

Edit the load balancer
1. Remove the nginx and api backends from the last release
2. Point `api-beta.monarchinitiative.org`, `api-v3.monarchinitiative.org`, and `api-next.monarchinitiative.org` to `monarch-v3-{release}-api-backend`
3. Point `next.monarchinitiative.org` and `monarchinitiative.org` to `monarch-v3-{release}-nginx-backend`
4. At the top of the host and path rules seciton, change the default backend ("Backend 1") to point to `monarch-v3-{release}-nginx-backend` as well

Then turn off the former production VMs (but keep them around for disaster recovery) by going to the GCP console VM listings and just clicking stop on each VM. 

Source the former former env in v3 stack to delete it (say yes to deleting, and no to creating in the terraform dialogs)
```
source site-envs/monarch-2023-10-17.env 
./provision.sh -d
```

