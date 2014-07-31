#-------------------------------------------------------------------------------
# Name:        category_mat_input
# Purpose:
#
# Author:      Animesh Pandey
#
# Created:     12/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import MySQLdb as mdb
import json
import sys
import numpy
import string

flatfile = 'allRestAttributes.dat'
jsonfile = 'business.json'
heading = 'attributes'

try:
    con = mdb.connect('localhost', 'root', 'root', 'yelp');
    replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))

    def toIdeal(temp_str):
        temp_str = temp_str.strip().translate(replace_punctuation)
        temp_str = temp_str.replace(" ", "_")
        temp_str = temp_str.replace("___", "_")
        return temp_str

    whole_list = []
    with open(flatfile, 'r') as f:
        for l in f:
            whole_list.append(toIdeal(l))

    all_categories = []
    temp = []
    ##count = 0
    with open(jsonfile, 'r') as f:
        for l in f:
            vector = [0]*len(whole_list)
    ##        count += 1
            line = l.strip()
            json_data = json.loads(line)
            temp = [toIdeal(str(i)) for i in json_data[heading]]
            all_categories.append(json_data[heading])

    ##        print [j for j in [whole_list.index(i) for i in temp]]

            for ind in [j for j in [whole_list.index(i) for i in temp]]:
                vector[ind] = vector[ind] + 1

    ##        print ''.join([str(i) for i in vector])

            try:
                query = "insert into bu_cat values(" + ','.join([str(i) for i in vector]) + ")"
                print query
##                with con:
##                    cur = con.cursor()
##                    cur.execute(query)
##                    con.commit()

            except mdb.Error, e:
                print e
                sys.exit(1)

    ##        if count == 4:
    ##            sys.exit(0)

except mdb.Error, e:
    print e
    sys.exit(1)

finally:
    if con:
        con.close()

