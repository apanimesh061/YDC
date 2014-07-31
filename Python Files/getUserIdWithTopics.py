#-------------------------------------------------------------------------------
# Name:        getUserIdWithTopics
# Purpose:     Map user IDs to the topics extracted using LDA.
#
# Author:      Animesh Pandey
#
# Created:     24/06/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import gensim
from gensim import corpora
import numpy as np
import json, ast

def epicSplit(length, chunk):
    arr = [chunk]*((length - length%chunk)/chunk)
    arr.append(length%chunk)
    return arr

def load_json(name):
    with open(name,  'r') as f:
        temp = []
        for l in f:
            l = l.strip()
            temp.append(l)
        json_data = json.loads(json.dumps(temp))
        return_dict = [ast.literal_eval(i) for i in json_data]
        return return_dict

content = load_json('review.json')
print epicSplit(len(content), 50000)
