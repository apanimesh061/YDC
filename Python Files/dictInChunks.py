from utility import *
import gensim
from gensim import corpora
import sys

count = 0

def epicSplit(length, chunk):
    arr = [chunk]*((length - length%chunk)/chunk)
    arr.append(length%chunk)
    return arr

def getTopicForComment (stoplist,  comment, dic, lda):
    global count
    count += 1
    temp = comment.lower()
    punctuation_string = '1234567890,/;-=+?><":|\/()?{}~`!@#$%^&*_.' + "'"
    for i in range(len(punctuation_string)):
        temp = temp.replace(punctuation_string[i], ' ')

    words = re.findall(r'\w+', temp, flags = re.UNICODE | re.LOCALE)
    
    important_words = filter(lambda x: x not in stoplist, words)

    ques_vec = dict_file.doc2bow(important_words)
    topic_vec = lda[ques_vec]
    
    word_count_array = numpy.empty((len(topic_vec), 2), dtype = numpy.object)

    for i in range(len(topic_vec)):
        word_count_array[i, 0] = topic_vec[i][0]
        word_count_array[i, 1] = topic_vec[i][1]

    try:
        idx = numpy.argsort(word_count_array[:, 1])
        idx = idx[::-1]
        word_count_array = word_count_array[idx]
        final = []
        final = lda.print_topic(word_count_array[0, 0], 50)
        # final = final.split('+')
        # temp_final = []
        # for f in final:
        #     temp_final.append(f.lstrip(' ').rstrip(' ').split('*'))
        # final = [temp_final[i][1] for i in range(len(temp_final))]
        # final = [t[0].upper() + t[1:] for t in final]
        return final

    except:
        smalltext = open('very_small_review.dat',  'a')
        smalltext.write(str(count) + "\n")
        smalltext.close()
        print word_count_array,  idx,  count
        return "-"

if __name__ == "__main__":

    json_file = 'review.json'
    corpusname = 'yelp_reviews.dat'
    dict_file = 'yelp_reviews.dict'
    model_file = 'yelp_review_LDAMODEL'

    chunk_size = 500

    stoplist = loadAllStopwords('allStopWords.dat')
    lda = gensim.models.ldamodel.LdaModel.load(model_file)
    dict_file = corpora.Dictionary.load('yelp_reviews.dict')

    all_text = readDatAndReturn(corpusname)
    all_bids = readDatAndReturn('rid_reviews.dat')

    zipper = zip(range(((len(all_text) - (len(all_text)%chunk_size))/chunk_size)), epicSplit(len(all_text), chunk_size)) + [(((len(all_text) - (len(all_text)%chunk_size))/chunk_size), (len(all_text)%chunk_size))]

    for idx, chunk in zipper:
        td = dict()

        if (idx == ((len(all_text) - (len(all_text)%chunk_size))/chunk_size)):
            print "From " + str(idx*chunk_size) + " to " + str(len(all_text)%chunk_size) + "..."
            for c, d in zip(all_bids[idx*chunk_size : len(all_text)], all_text[idx*chunk_size : len(all_text)]):
                # print {c.strip():",".join(getTopicForComment(stoplist, d, dict_file, lda))}
                td.update({c.strip():",".join(getTopicForComment(stoplist, d, dict_file, lda))})
        else:
            # continue
            print "From " + str(idx*chunk_size) + " to " + str(chunk*(idx+1)) + "..."
            for c, d in zip(all_bids[idx*chunk_size:chunk*(idx+1)], all_text[idx*chunk_size:chunk*(idx+1)]):
                # print {c.strip():",".join(getTopicForComment(stoplist, d, dict_file, lda))}

                td.update({c.strip() : getTopicForComment(stoplist, d, dict_file, lda)})

        createPickleFromDict(td, 'bu_topics_prob' + str(idx) + '.pkl')
        print "Mere naal tu whistle bajaaa ..."
        break