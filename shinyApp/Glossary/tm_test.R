library(SnowballC)
library(tm)
library(arules)


# load in terms and definitions

# convert to format for text mining: term label- vocabulary concatenation/ definition

#read as 
df<-distinct(data[c("uri","Definition","Term","Vocabulary")],uri,.keep_all=T)
colnames(df)[1]<-"doc_id"
colnames(df)[2]<-"text"

my.corpus <- Corpus(DataframeSource(df))

#remove punctuation and stopwords and lemmatize (remove plurals and hyphenation and such)
my.corpus <- tm_map(my.corpus, removePunctuation)
my.corpus <- tm_map(my.corpus, removeWords, stopwords("english"))

my.corpus <- tm_map(my.corpus, stemDocument)

#Process to matrix
tdm <- TermDocumentMatrix(tm::inspect(my.corpus))


library(slam)
cosine_dist_mat <- 1 - crossprod_simple_triplet_matrix(tdm)/(sqrt(col_sums(tdm^2) %*% t(col_sums(tdm^2))))


tdm <- as.matrix(tdm)
require(proxy)
cosine_dist_mat <- as.matrix(dist(t(tdm), method = "cosine"))

#scale word counts

#calculate cosine dissimilarity matrix

#cluster

#cut tree

#list of term-vocabularies by cluster