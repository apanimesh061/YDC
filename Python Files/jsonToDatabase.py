#-------------------------------------------------------------------------------
# Name:        jsonToDatabase
# Purpose:     decode JSON to Database data
#
# Author:      Animesh Pandey
#
# Created:     05/03/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import json
import sys
from pprint import pprint

def getDictAttributes(d):
    for i, j in d.iteritems():
        if (isinstance(j, dict)):
            print i
            getDictAttributes(j)
        else:
            pass
##            print "{0} : {1}".format(i, j)

count = 0
temp = []
with open('test.json') as f:
    for l in f:
        count += 1
        line = l.strip()
        json_data = json.loads(line)

        temp.append(line)

##        pprint(json_data)
        getDictAttributes(json_data)

        if count == 1:
            sys.exit(0)
