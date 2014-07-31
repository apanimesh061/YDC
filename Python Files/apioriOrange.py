#-------------------------------------------------------------------------------
# Name:        Apriori Algorithm for categories
# Purpose:
#
# Author:      Animesh Pandey
#
# Created:     19/07/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import Orange
import sys
import numpy as np
import csv

with open('allRestCategories.dat', 'r') as f:
    cats = f.readlines()

def convertListToCat(l):
    temp = [i for i in l.split(' ')]
    temp.remove('->')
    return [categories[int(i)] for i in temp]
##    return list(set([int(i) for i in temp]))

def csv_writer(data, path):
    with open(path, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def removeRedundanciesFromLol(k):
    import itertools
    k.sort()
    return list(k for k,_ in itertools.groupby(k))

if __name__ == '__main__':

    categories = [c.strip() for c in cats]
    data = Orange.data.Table("patterns.basket")
    rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.004)

    pattern_data = []
    category_list = []
    for r in rules:
        category_list.append(convertListToCat(str(r)))
        pattern_data.append([str(r.support), str(r.confidence), str(r.coverage), str(r.strength), str(r.lift), str(r.leverage), ';'.join(convertListToCat(str(r)))])

##    csv_writer(pattern_data, 'dataAndCatPatterns.csv')

    asd = np.asmatrix(pattern_data).transpose()
    finalCatPatterns = removeRedundanciesFromLol(category_list)
