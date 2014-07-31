import cPickle,  json,  ast, re
import numpy

import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

import gensim
from gensim import corpora, similarities, models

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def sliceList(n, iterable):
    from itertools import islice
    return list(islice(iterable, n))

def mergeListOfLists(l):
    return sum(l, [])

def load_obj(name):
    print "Loading " + name
    with open(name, 'rb') as f:
        return cPickle.load(f)

def sliceDictionary(n,  iterable):
    from itertools import islice
    from operator import itemgetter
    my_list = list(islice(iterable, n))
    return zip(my_list, itemgetter(*my_list)(iterable))

def load_json(name):
    with open(name,  'r') as f:
        temp = []
        for l in f:
            l = l.strip()
            temp.append(l)
        json_data = json.loads(json.dumps(temp))
        return_dict = [ast.literal_eval(i) for i in json_data]
        return return_dict

def createDictWithListAsValues(datafile, keyval, valueval):
    from collections import defaultdict
    theList = []
    with open(datafile,  'rb') as f:
        for line in f:
            line = line.strip()
            json_data = json.loads(line)
            theList.append((json_data[keyval], json_data[valueval]))
    d = defaultdict(list)
    for a, b in theList:
        d[a].append(b)
    d = dict(d)
    return d

def printDictTillRange(d,  r):
    count = 0
    for a, b in d.iteritems():
        count += 1
        print  a,  b[0]
        if count == r:
            break

def createPickleFromDict(d,  filename):
    cPickle.dump(d,  open(filename,  "wb"))
    print 'Pickled ' + filename

def readDatAndReturn(filename):
    with open(filename) as f:
        returned_list = f.readlines()
    return returned_list

def loadAllStopwords(sw_path):
    stoplist = nltk.corpus.stopwords.words('english')
    stopwords_list_II = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,send,ignore,number,change,creating,external,values,page,line,test,file,time,images,way,use,first,second,third,using,one,two,three,four,five,six,seven,eight,nine,ten,next,way,look,wasnt,doesnt,hadnt,didnt,couldnt,using,always,within,required,getting,another,a,as,able,about,above,according,accordingly,across,actually,after,afterwards,again,against,ain,t,all,allow,allows,almost,alone,along,already,also,although,always,am,among,amongst,an,and,another,any,anybody,anyhow,anyone,anything,anyway,anyways,anywhere,apart,appear,appreciate,appropriate,are,aren,t,around,as,aside,ask,asking,associated,at,available,away,awfully,be,became,because,become,becomes,becoming,been,before,beforehand,behind,being,believe,below,beside,besides,best,better,between,beyond,both,brief,but,by,c,mon,c,s,came,can,can,t,cannot,cant,cause,causes,certain,certainly,changes,clearly,co,com,come,comes,concerning,consequently,consider,considering,contain,containing,contains,corresponding,could,couldn,t,course,currently,definitely,described,despite,did,didn,t,different,do,does,doesn,t,doing,don,t,done,down,downwards,during,each,edu,eg,eight,either,else,elsewhere,enough,entirely,especially,et,etc,even,ever,every,everybody,everyone,everything,everywhere,ex,exactly,example,except,far,few,fifth,first,five,followed,following,follows,for,former,formerly,forth,four,from,further,furthermore,get,gets,getting,given,gives,go,goes,going,gone,got,gotten,greetings,had,hadn,t,happens,hardly,has,hasn,t,have,haven,t,having,he,he,s,hello,help,hence,her,here,here,s,hereafter,hereby,herein,hereupon,hers,herself,hi,him,himself,his,hither,hopefully,how,howbeit,however,i,d,i,ll,i,m,i,ve,ie,if,ignored,immediate,in,inasmuch,inc,indeed,indicate,indicated,indicates,inner,insofar,instead,into,inward,is,isn,t,it,it,d,it,ll,it,s,its,itself,just,keep,keeps,kept,know,knows,known,last,lately,later,latter,latterly,least,less,lest,let,let,s,like,liked,likely,little,look,looking,looks,ltd,mainly,many,may,maybe,me,mean,meanwhile,merely,might,more,moreover,most,mostly,much,must,my,myself,name,namely,nd,near,nearly,necessary,need,needs,neither,never,nevertheless,new,next,nine,no,nobody,non,none,noone,nor,normally,not,nothing,novel,now,nowhere,obviously,of,off,often,oh,ok,okay,old,on,once,one,ones,only,onto,or,other,others,otherwise,ought,our,ours,ourselves,out,outside,over,overall,own,particular,particularly,per,perhaps,placed,please,plus,possible,presumably,probably,provides,que,quite,qv,rather,rd,re,really,reasonably,regarding,regardless,regards,relatively,respectively,right,said,same,saw,say,saying,says,second,secondly,see,seeing,seem,seemed,seeming,seems,seen,self,selves,sensible,sent,serious,seriously,seven,several,shall,she,should,shouldn,t,since,six,so,some,somebody,somehow,someone,something,sometime,sometimes,somewhat,somewhere,soon,sorry,specified,specify,specifying,still,sub,such,sup,sure,t,s,take,taken,tell,tends,th,than,thank,thanks,thanx,that,that,s,thats,the,their,theirs,them,themselves,then,thence,there,there,s,thereafter,thereby,therefore,therein,theres,thereupon,these,they,they,d,they,ll,they,re,they,ve,think,third,this,thorough,thoroughly,those,though,three,through,throughout,thru,thus,to,together,too,took,toward,towards,tried,tries,truly,try,trying,twice,two,un,under,unfortunately,unless,unlikely,until,unto,up,upon,us,use,used,useful,uses,using,usually,value,various,very,via,viz,vs,want,wants,was,wasn,t,way,we,we,d,we,ll,we,re,we,ve,welcome,well,went,were,weren,t,what,what,s,whatever,when,whence,whenever,where,where,s,whereafter,whereas,whereby,wherein,whereupon,wherever,whether,which,while,whither,who,who,s,whoever,whole,whom,whose,why,will,willing,wish,with,within,without,won,t,wonder,would,would,wouldn,t,yes,yet,you,you,d,you,ll,you,re,you,ve,your,yours,yourself,yourselves,zero,re".split(',')
    sw = readDatAndReturn(sw_path)
    stoplist = stoplist + sw + stopwords_list_II
    stoplist = list(set(stoplist))
    stoplist = [i.encode('utf-8') for i in stoplist]
    return stoplist

def createTextCorpusFromDBQuery(dbquery, database,  username,  password, corpusname):
    import MySQLdb
    punctuation_string = '1234567890,/;-=+?><":|\/()?{}~`!@#$%^&*_.' + "'"
    try:
        final_text = []
        con = MySQLdb.connect('localhost', username, password, database)
        con.query('SET GLOBAL connect_timeout=28800')
        con.query('SET GLOBAL wait_timeout=28800')
        con.query('SET GLOBAL interactive_timeout=28800')
        with con:
            cur = con.cursor()
            cur.execute(dbquery)
            rows = cur.fetchall()
            text_list = []
            for row in rows:
                temp = str(row[0])
                for i in range(len(punctuation_string)):
                    temp = temp.replace(punctuation_string[i], ' ')
                text_list.append(" ".join(temp.split()).decode('cp1252').encode('utf-8'))
            f = open(corpusname,  "w")
            for line in text_list:
                f.write(line + "\n")
            f.close()
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        print "Database read."
        if con:
            con.close()
    
    print "Corpus created."
    return text_list

def createTextCorpusFromJson(json_file,  corpusname):
    punctuation_string = '1234567890,/;-=+?><":|\/()?{}~`!@#$%^&*_.' + "'"
    d = load_json(json_file)
    text_list = []
    for row in d:
        temp = str(row['text'])
        for i in range(len(punctuation_string)):
            temp = temp.replace(punctuation_string[i], ' ')
        text_list.append(" ".join(temp.split()).decode('cp1252').encode('utf-8'))
    f = open(corpusname,  "w")
    for line in text_list:
        f.write(line + "\n")
    f.close()
    print "Corpus created."
    return text_list

def createDictFromCorpus(filename):
    stoplist = loadAllStopwords('allStopWords.dat')
    dictionary = corpora.Dictionary(line.lower().split() for line in open(filename,  'r'))
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    dictionary.filter_tokens(stop_ids + once_ids)
    print "Removal of stop words done."
    dictionary.compactify()
    print "Dictionary created."
    dictionary.save(filename[:-4]+".dict")
    return filename[:-4]+".dict"

def createMMCorpusFromDict(filename,  final_text):
    dictionary = corpora.Dictionary.load(filename[:-4] + ".dict")
    corpus = [dictionary.doc2bow(text.split()) for text in final_text]
    corpora.MmCorpus.serialize(filename[:-4] + ".mm", corpus)
    print "Market Matrix created. Now will perform LDA on it."
    return filename[:-4]+".mm"

def performLDA(dictionaryname, corpus, chunksize, num_topics, passes):
    print "Hold your horses, LDA now begins ...."
    mm = corpora.MmCorpus(corpus)
    dictionary = corpora.Dictionary.load(dictionaryname)
    lda = gensim.models.ldamodel.LdaModel(
                                          corpus = mm, 
                                          id2word = dictionary, 
                                          num_topics = num_topics, 
                                          update_every = 0, 
                                          chunksize = chunksize, 
                                          passes = passes
                                          )
    return lda

# def getTopicForComment (comment, dic, lda):

#     temp = comment.lower()
#     punctuation_string = '1234567890,/;-=+?><":|\/()?{}~`!@#$%^&*_.' + "'"
#     for i in range(len(punctuation_string)):
#         temp = temp.replace(punctuation_string[i], ' ')

#     words = re.findall(r'\w+', temp, flags = re.UNICODE | re.LOCALE)

#     stoplist = loadAllStopwords('allStopWords.dat')
#     important_words = filter(lambda x: x not in stoplist, words)

#     #text_list.append(" ".join(temp.split()).decode('cp1252').encode('utf-8'))
#     dictionary = corpora.Dictionary.load(dic)
#     ques_vec = dictionary.doc2bow(important_words)
#     topic_vec = lda[ques_vec]
    
#     word_count_array = numpy.empty((len(topic_vec), 2), dtype = numpy.object)

#     for i in range(len(topic_vec)):
#         word_count_array[i, 0] = topic_vec[i][0]
#         word_count_array[i, 1] = topic_vec[i][1]

#     idx = numpy.argsort(word_count_array[:, 1])
#     idx = idx[::-1]
#     word_count_array = word_count_array[idx]
    
#     final = []
#     final = lda.print_topic(word_count_array[0, 0], 50)
#     final = final.split('+')
#     temp_final = []
    
#     for f in final:
#         temp_final.append(f.lstrip(' ').rstrip(' ').split('*'))
    
#     final = [temp_final[i][1] for i in range(len(temp_final))]
#     del(temp_final)
#     final = [t[0].upper() + t[1:] for t in final]
    
#     return final

def mergeDictionries(*arg):
    d = []
    [d.append(load_obj(filename)) for filename in arg[:-1]]
    
    mergedDict = dict()
    mergedDict.update(d[0])
    [mergedDict.update(k) for k in d[1:]]
    
    createPickleFromDict(mergedDict, arg[-1])
