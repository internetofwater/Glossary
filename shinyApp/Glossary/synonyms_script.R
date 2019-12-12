

###Querying synonyms of homoynms
d<-distinct(data,uri,.keep_all=TRUE)
hom_parse<-paste0('PREFIX :<http://www.ontotext.com/graphdb/similarity/>
PREFIX inst:<http://www.ontotext.com/graphdb/similarity/instance/>
PREFIX pubo: <http://ontology.ontotext.com/publishing#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?uri {
    ?search a inst:term_similarity ;
        :searchDocumentID <http://purl.org/iow/terms/c_1d21b254>;
        :documentResult ?result .
 ?result :value ?uri ;
            :score ?score.
     FILTER(?score = 1) .
    OPTIONAL{ ?uri skos:exactMatch ?uri2.} 
}')

syn_parse<-"PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?uri ?uri2 {
 ?uri skos:exactMatch ?uri2

}"

hom_parse<-paste0('PREFIX :<http://www.ontotext.com/graphdb/similarity/>
PREFIX inst:<http://www.ontotext.com/graphdb/similarity/instance/>
PREFIX pubo: <http://ontology.ontotext.com/publishing#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?uri {
    ?search a inst:term_similarity ;
        :searchDocumentID <http://purl.org/iow/terms/c_1d21b254>;
        :documentResult ?result .
 ?result :value ?uri ;
            :score ?score.
     FILTER(?score = 1) .
    OPTIONAL{ ?uri skos:exactMatch ?uri2.} 
}')
hom_uris<-SPARQL(endpoint,hom_parse,format="csv")$result
hom_uris
unique(hom_uris)
x<-c(hom_uris$uri,hom_uris$uri2)
x
x<-c(as.character(hom_uris$uri),as.character(hom_uris$uri2))


#clus<-reactive({
syn_graph<-SPARQL(endpoint,syn_parse,format="csv")$result%>%mutate(uri=as.character(uri),uri2=as.character(uri2))

syn_graph<-as.matrix(syn_graph)
syn_graph<-graph_from_edgelist(syn_graph)
clu<-as.data.frame(components(syn_graph)$membership)
clu$uri<-rownames(clu)
rownames(clu)<-NULL
colnames(clu)<-c("Definition Group","uri")
clu<-clu[c(2,1)]

#})

d<-d%>%left_join(clu,by="uri")

##create graph

##identify subcomponents

##create table