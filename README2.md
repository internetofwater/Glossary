# Glossary
An ontology of water, data, and internal IoW concepts, with definitions and provenance

# Overall organization

There are three components of the Internet of Water Glossary (new name reccomended by the Board of Advisors TBD)

1. A vocabulary management system where terms are ingested into a [SKOS](https://www.w3.org/2004/02/skos/)-compliant RDF and semantic links (skos:related and skos:exactMatch) are drawn between terms. We use [VocBench3](http://vocbench.uniroma2.it/). Our implementation is at [http://purl.org/iow/vocbench3](http://purl.org/iow/vocbench3). It is a docker image of VocBench v.3.6.0.0 (see our [repository](https://github.com/internetofwater/docker-vocbench3))

2. A graph database where the vocabulary management system stores the data. The graph database also has an open SPARQL endpoint from which the data can be queried. Currently the graph database is internal to our VocBench. Soon, we will implement a separate one as a standalone [GraphDB]() server2. A graph database where the vocabulary management system stores the data. The graph database also has an open SPARQL endpoint from which the data can be queried. Currently the graph database is internal to our VocBench. Soon, we will implement a separate one as a standalone [GraphDB](http://graphdb.ontotext.com/) server

3. A front-end browser
