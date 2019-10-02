library(SnowballC)
library(tm)
library(arules)


# load in terms and definitions

# convert to format for text mining: term label- vocabulary concatenation/ definition

#read as corpus
my.corpus <- Corpus(DirSource("corpus/r-corpus"))

#remove punctuation and stopwords and lemmatize (remove plurals and hyphenation and such)
my.corpus <- tm_map(my.corpus, removePunctuation)
my.corpus <- tm_map(my.corpus, removeWords, stopwords("english"))

my.corpus <- tm_map(my.corpus, stemDocument)

#Process to matrix
my.tdm <- TermDocumentMatrix(tm::inspect(my.corpus))

#scale word counts

#calculate cosine dissimilarity matrix

#cluster

#cut tree

#list of term-vocabularies by cluster