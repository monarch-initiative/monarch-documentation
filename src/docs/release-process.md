# Monarch Release Process

## Overview

This document describes the steps required to create a new Monarch release.  

These releases consist primarily of the following components:  

- Monarch Mapping files via [Monarch Mapping Commons](https://github.com/monarch-initiative/monarch-mapping-commons)
- Knowledge Graph via [Monarch Ingest](https://github.com/monarch-initiative/monarch-ingest)
- Data library and API via [Monarch-Py](https://github.com/monarch-initiative/monarch-app/backend)
- Monarch website via [Monarch-App](https://github.com/monarch-initiative/monarch-app/frontend)


## Monarch Mapping Commons

[Monarch Mapping Commons](https://github.com/monarch-initiative/monarch-mapping-commons) is a repository that contains code used to generate the mapping files used in the creation of the Monarch knowledge graph.  
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

Preparing the environment for deployment:

* Make sure dependancies from monarch-stack-v3/README.md are installed
* Ensure secrets are installed in $home/.secrets

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

Once work on the milestone is complete, we need to tag the release in GitHub then we can deploy to the beta environment.

To tag the release, go to the [Monarch App](https://github.com/monarch-initiative/monarch-app) and click on releases. Create a new release with the new version number and click generate release notes. Make any changes to the release notes that are necessary (generally none) and click publish release.

You may want to set an environment variable for the release version to make it easier to copy and paste the version number in the following steps (update for your current version):

```
RELEASE="2026-09-02"
```

> **The steps below run from a checkout of [monarch-stack-v3](https://github.com/monarch-initiative/monarch-stack-v3), using its `just` recipes.**
> Each one prints what it is about to change, prompts before doing it, and verifies the result afterwards.
> Run `just` with no arguments to list them, and `just kg-status ${RELEASE}` at any point to see how far along a release is.

First, publish the KG build from `monarch-kg-dev` into the public release path:

```
just kg-publish ${RELEASE}
```

This is a curation gate rather than a formality: `monarch-kg-dev` also holds builds that were never released and scratch prefixes, and everything under `monarch-kg` is a real release. The recipe refuses a build missing any artifact the stack needs (`solr.tar.gz`, `monarch-kg.duckdb`, `phenio.db.gz`), so an incomplete build cannot become one.

**It has to run before you provision the stack.** Site-envs point `MONARCH_DATA_URL` at `monarch-kg`, and the stack stages its data at provision time — a stack built before the copy has nothing to pull.

> **Note — a step that has quietly stopped happening.** Earlier versions of this document also copied the release into `gs://monarch-archive/monarch-kg/`.
> That has not been done since **2025-01-15**; no 2026 release is present there.
> Either revive it (and automate it alongside the rest) or drop it deliberately — at the moment the documentation and reality disagree.

Within monarch-stack-v3, copy the latest release env file to a new env, for example: `cp site-envs/monarch-2026-08-20.env site-envs/monarch-${RELEASE}.env`
The date for the environment file name should match the KG release version, rather than today's date. 
Edit the top two lines in new env to match the latest KG & API versions:

```
export MONARCH_KG_VERSION="2026-09-02"
export MONARCH_API_VERSION="1.30.0"
```

Then source the new environment and run provision.sh to create the new VM stack, paying attention to the terrform output to make sure that it's creating VMs with a version name you expect:

```
source site-envs/monarch-2023-11-16.env
./provision.sh
```

Output for the provision script should look something like this:

```
...
Changes to Outputs:
  + api_image_tag       = "1.0.0"
  + env                 = "2024-02-13"
  + full_prefix         = "monarch-v3-2024-02-13-"
  + neo4j_archive_url   = "https://data.monarchinitiative.org/monarch-kg-dev/latest/monarch-kg.neo4j.dump"
  + phenio_archive_url  = "https://data.monarchinitiative.org/monarch-kg/2024-02-13/phenio.db.gz"
  + project             = "monarch-initiative"
  + semsimian_image_tag = "latest"
  + solr_archive_url    = "https://data.monarchinitiative.org/monarch-kg/2024-02-13/solr.tar.gz"
  + sqlite_archive_url  = "https://data.monarchinitiative.org/monarch-kg/2024-02-13/monarch-kg.db.gz"
  + stack               = "monarch-v3"
  + ui_image_tag        = "latest"
  + vm_svc_acct_email   = "terraform@monarch-initiative.iam.gserviceaccount.com"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
```

At the end of the run you should see a message like this:

```
PLAY RECAP ***************************************************************************************************
monarch-v3-2024-02-13-api  : ok=11   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
monarch-v3-2024-02-13-manager : ok=12   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
monarch-v3-2024-02-13-neo4j : ok=11   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
monarch-v3-2024-02-13-solr : ok=11   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

#### Connecting beta to the load balancer

```
just lb-beta ${RELEASE}
```

That points both `beta.monarchinitiative.org` and `api-beta.monarchinitiative.org` at the new stack, then polls until both actually report the new KG version.

**Do not edit the load balancer by hand in the GCP console.** Host rules are matched by exact string and a misspelled hostname does not error — it simply never matches, so requests fall through to the url-map's default service and are quietly served by the *previous* stack, with nothing in any log to catch it. That has happened: a rule reading `beta.monarchinitiiative.org` (doubled `i`) left beta serving the old stack for as long as it was believed to be live. `api-beta` was spelled correctly, so the API looked healthy and only the UI showed stale data.

The recipes exist to remove both conditions: hostnames are declared once in `deployment/lb.py` and never typed, and routing changes repoint a path matcher's backend rather than rewriting host rules.

Useful alongside it:

```
just lb-show                      # which stack each hostname is served by
just lb-check                     # flag any host rule that can never match
just lb-verify ${RELEASE} beta    # re-poll without changing anything
```

Verification asks the real hostname which KG version it is serving, via `/v3/api/version`. Check it **through the UI hostname**, not just the API one — that is the check a misspelled UI rule cannot pass.

Expect the load balancer to take a few minutes. Config propagates per edge location, so for a while different locations legitimately disagree; the recipes poll rather than checking once.

Get yourself a cup of hot chocolate / ice cold lemonade (season dependent) and settle in to go through the issues in the milestone. Make sure that each issue appears to actually be fixed, and close them with a note that they're confirmed to be working on beta.monarchinitiative.org. (with some additional explanation for externally submitted issues about when the change is expected to be visible on the production site)


#### Deploying to production

Once beta looks good, one command does the whole promotion:

```
just promote ${RELEASE}
```

It prints the current state, shows exactly what will change, asks once, and then:

1. syncs `gs://.../monarch-kg/${RELEASE}` over `.../monarch-kg/latest`
2. regenerates the `index.html` directory listings under `latest/`
3. publishes the monarch-ingest draft release, which creates the git tag
4. points `monarchinitiative.org`, `api-v3`, `api`, and `dev`/`kg`/`next` at the new stack, then polls until they serve it

Every step is individually re-runnable, so a promotion that fails partway is resumed by running it again: the bucket sync is an rsync, publishing an already-published release is a no-op, and repointing routing that is already correct is a no-op. The individual steps are also available on their own (`just kg-latest`, `just kg-release`, `just lb-promote`) if you want to do part of it.

The `latest` sync uses `gcloud storage rsync` rather than `rm` followed by `cp`. The older manual form deleted `latest` — a public download path — for the duration of a ~56 GiB copy, and left it empty or partial if the copy failed.

#### Retiring the old stacks

After a promotion there are normally three stacks alive: the new one serving production, the previous one kept as a warm fallback, and the one behind that which is no longer needed.

```
just stacks                          # VM states + which hostnames each stack serves
just stack-stop <previous-release>   # outgoing stack -> fallback (VMs off, kept)
just stack-destroy <older-release>   # the one behind it -> gone
```

Stopping keeps the VMs present so the stack can be restarted and routed back to in minutes without a rebuild. Destroying is terraform, because a stack is more than VMs — backend services, NEGs, health checks and firewall rules all go together.

Both refuse to touch a stack that any hostname still routes to, checked against the live load balancer rather than assumed. `stack-destroy` additionally refuses a stack whose VMs are still running, so nothing can go from serving traffic straight to destroyed without passing through the fallback stage, and it asks you to type the env name rather than just `y`.

#### Troubleshooting

Here are some known issues that we have seen before:

In `./provision.sh` you may see an error like this:

```
fatal: [monarch-v3-2024-02-13-api]: UNREACHABLE! => changed=false
  msg: |-
    Data could not be sent to remote host "monarch-v3-2024-02-13-api". Make sure this host can be reached over ssh: Pseudo-terminal will not be allocated because stdin is not a terminal.
    sa_116692422516913491665@34.42.108.156: Permission denied (publickey).

    Recommendation: To check for possible causes of SSH connectivity issues and get
    recommendations, rerun the ssh command with the --troubleshoot option.

    gcloud compute ssh monarch-v3-2024-02-13-api --project=monarch-initiative --zone=us-central1-a --troubleshoot

    Or, to investigate an IAP tunneling issue:

    gcloud compute ssh monarch-v3-2024-02-13-api --project=monarch-initiative --zone=us-central1-a --troubleshoot --tunnel-through-iap

    ERROR: (gcloud.compute.ssh) [/usr/bin/ssh] exited with return code [255].
  unreachable: true
```

If so you may want to run the stated command (update to your version):

```commandline
gcloud compute ssh monarch-v3-2024-02-13-api --project=monarch-initiative --zone=us-central1-a --troubleshoot
```

