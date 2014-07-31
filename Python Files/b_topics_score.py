from utility import *
import csv
import cPickle
import matplotlib.pyplot as plt

def normalizeList(num_list):
    return map(lambda x: x / float(sum(num_list)), num_list)

# all_topics = load_obj('bu_topics_50.pkl')
# review_data = load_json('review.json')
# noCat = readDatAndReturn('underNoCategory.dat')
all_stars  = load_obj('ridToStars.pkl')
all_scores = load_obj('ridToSS.pkl')
# br = load_obj('bidToRid.pkl')

stars = all_stars.values()
scores = [int(i.strip()) for i in all_scores.values()]

chunk = 10000

##plt.scatter(scores[:chunk], stars[:chunk], color='r')
####plt.scatter(range(len(all_stars))[:chunk], normalizeList(scores[:chunk]), color='b')
##plt.grid()
##plt.show()

from sklearn import svm
X = [[s] for s in scores[:chunk]]
Y = stars[:chunk]
clf = svm.SVC()
clf.fit(X, Y)

# bid_topics = dict()
# bid_sentiment_scores = dict()

# for bid, rids in br.iteritems():
# 	temp_topic = []
# 	temp_score = []
# 	for rid in rids:
# 		temp_topic.append(all_topics[rid].split(','))
# 		temp_score.append(int(all_scores[rid].strip()))
# 	bid_topics.update({bid : list(set(sum(temp_topic, [])))})
# 	bid_sentiment_scores.update({bid : temp_score})

# cPickle.dump(bid_topics, open("bid_topics.pkl",  "wb"))
# cPickle.dump(bid_sentiment_scores, open("bid_sentiment_scores.pkl",  "wb"))
