import cPickle
import sys
import json,  ast

def load_obj(name):
    with open(name, 'rb') as f:
        return cPickle.load(f)

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
        print "File opened for reading..."
        for line in f:
            line = line.strip()
            json_data = json.loads(line)
            theList.append((json_data[keyval],  json_data[valueval]))

    print "whole file has been read..."
    d = defaultdict(list)
    for a, b in theList:
        d[a].append(b)
    d = dict(d)
    print "dictionary created..."
    return d

# cbu_list = load_obj("cbu.pkl")

#users = load_json('review.json')

d = createDictWithListAsValues('review.json',  'review_id',  'text')

cPickle.dump(d, open("ridToText.pkl",  "wb"))

print "Dumped!"
