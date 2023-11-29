## Monarch role: Mondo technical lead

Main responsibilities:

1. [Coordinate the development of the Mondo ingest pipeline](#ingest)
1. Ensure the ongoing Mondo ingest pipeline with external sources runs smoothly (devops)
1. Support the curation team:
    1. Ensure that the release system (including import management, ODK stuff etc) runs smoothly (mostly support / debugging role when things break because of a bad imported axiom or a software update).
    1. Maintain and extend the QC system. The curation team identifies and issue that needs a check. We develop it and integrate it into the QC system
    1. General debugging support for Curation team 'when things break'
1. Communicate with technical stakeholders (mainly NORD, ClinGen). Mostly support role, but sometimes requirements gathering which are fed back to curation team (eg rare disease subset, release notification endpoint).
1. Lead ongoing processes to clean and standardise metadata inside the ontology.
1. Communicate with external stakeholders such as MedGen and ClinGen about technical issues

<a id="ingest"></a>

## Coordination of the Mondo Ingest pipeline

Github: https://github.com/monarch-initiative/mondo-ingest
Documentation: https://monarch-initiative.github.io/mondo-ingest/

### Develop an efficient system for aligning external ontologies

The most important _technical_ component of Mondo is its alignment system. It comprises a number of sub-systems. The three core subsystems are:

1. Mapping system (map new terms in external ontologies to Mondo)
2. Migrations system (incorporate new terms from external resources into Mondo)
3. Syncing system (update information about terms already mapped in Mondo)

## Incorporating new ingests

As there are dozens of resources that _could_ be incorporated, but our curation resources are limited,
we need to carefully decide which ingests to incorporate, strategically. Two ingests that are top priority for example are:

1. ICD10
1. ICD11

