#-------------------------------------------------------------------------------
# Name:        category_matrix
# Purpose:     make category mapping
#
# Author:      Animesh Pandey
#
# Created:     12/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import MySQLdb as mdb
import json, sys
import string

tableName = 'bu_att'
flatfile = 'allRestAttributes.dat'

replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))

def toIdeal(temp_str):
    temp_str = l.strip().translate(replace_punctuation)
    temp_str = temp_str.replace(" ", "_")
    temp_str = temp_str.replace("___", "_")
    return temp_str

whole_list = []
initials = "create table " + tableName + " ("

with open(flatfile, 'r') as f:
    for l in f:
        t = toIdeal(l) + " tinyint(1) default 0"
        whole_list.append(t)

query = json.dumps(initials + ','.join(whole_list) + ");")[1:-1]

try:
    con = mdb.connect('localhost', 'root', 'root', 'yelp');
    with con:
        cur = con.cursor()
        cur.execute(query)

except mdb.Error, e:
    print e
    sys.exit(1)

finally:
    if con:
        con.close()

