setwd("E:/yelp")

library(twitteR)
library(ROAuth)
library(ggplot2)
library(plyr)
library(stringr)

score.sentiment = function(sentences, pos.words, neg.words,.progress='none') {
  require(plyr)
  require(stringr)
  scores = laply(sentences, function(sentence, pos.words, neg.words) {
    sentence = gsub(":)", 'awsum', sentence)
    sentence = gsub('[[:punct:]]', '', sentence)  
    sentence = gsub('[[:cntrl:]]', '', sentence)  
    sentence = gsub('\\d+', '', sentence)  
    sentence = tolower(sentence)  
    
    word.list = str_split(sentence, '\\s+')  
    words = unlist(word.list)  
    
    pos.matches = match(words, pos.words)  
    neg.matches = match(words, neg.words)  
    pos.matches = !is.na(pos.matches)  
    neg.matches = !is.na(neg.matches)
    
    score = sum(pos.matches) - sum(neg.matches)  
    return(score)  
  }, pos.words, neg.words, .progress=.progress )  
  scores.df = data.frame(score=scores, text=sentences)  
  return(scores.df)  
}

hu.liu.pos = scan('positive-words.txt', what='character', comment.char=';')
hu.liu.neg = scan('negative-words.txt', what='character', comment.char=';')

pos.words = c(hu.liu.pos, 'upgrade', 'awsum')
neg.words = c(hu.liu.neg, 'wtf', 'wait','waiting', 'epicfail')

print("Loading all yelp reviews ...")
res <- readLines('yelp_reviews.dat')
print("All reviews loaded ...")

print("Now calculating scores")
yelpScores = score.sentiment(res, pos.words, neg.words, .progress='text')
print("Writing Scores to CSV ...")
write.csv(yelpScores, file=("yelp_reviews_scores.csv"), row.names=TRUE)
print("Complete!")

m <- ggplot(yelpScores, aes(x=score))
m + geom_histogram()
m + geom_histogram(aes(fill = ..count..))
