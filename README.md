# Glossary
An ontology of water, data, and internal IoW concepts, with definitions and provenance.

## Overall organization

There are three components of the Internet of Water Glossary (new name reccomended by the Board of Advisors TBD)

1. A vocabulary management system where terms are ingested into a [SKOS](https://www.w3.org/2004/02/skos/)-compliant RDF and semantic links (skos:related and skos:exactMatch) are drawn between terms. We use [VocBench3](http://vocbench.uniroma2.it/). Our implementation is at [http://purl.org/iow/vocbench3](http://purl.org/iow/vocbench3). It is a docker image of VocBench v.3.6.0.0 (see our [repository](https://github.com/internetofwater/docker-vocbench3))

2. A graph database implemented with [Ontotext GraphDB](http://graphdb.ontotext.com/) free edition where the vocabulary management system stores the ontology. Our GraphDB has two databases within it. First, a live database connected directly to VocBench and only accessible via VocBench or to database admins. Second, a mirror that has an open SPARQL endpoint for SELECT queries. This mirror also builds an [index of textual similarity](http://graphdb.ontotext.com/documentation/standard/semantic-similarity-searches.html) of definition.vWeekly, the live database is re-mirrored, and dumps of the database are made to JSON-LD files in this repository's [backup folder](https://github.com/internetofwater/Glossary/Backups)

3. A front-end browser. Currently this is a shiny app hosted by RStudio's free cloud hosting service here: [http://purl.org/iow/Glossary](http://purl.org/iow/GlossaryBrowser). The shiny app queries the mirror of the graph database via SPARQL. The browser also serves the important function of querying the similarity index to allow for human identification of synonyms (terms with equivalent definitions)



## Stuff in this repository

1. Template.xlsx, a template to be filled out for each vocabulary we ingest. Please rename to a suitable concatenation of agency and vocabulary (e.g. epa-abg for 'EPA Aquatic Biodiversity Glossary'), and push to an appropriate organization-level folder in the 'Vocabularies' folder in this repository.

2. excel_vocab_import.pr, a script to wrap and ingest a filled-in xlsx template into the RDF graph using VocBench3
