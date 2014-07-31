#-------------------------------------------------------------------------------
# Name:        dbscan_labels
# Purpose:     Reading the DBSCAN Cluster labels
#
# Author:      Animesh Pandey
#
# Created:     20/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

##with open('dbscan_labels.dat', 'r') as f:
##    content = f.readlines()
##
##labels = [int(float(e.strip())) for e in content]
##
##print labels

import json, sys, csv, urllib2

filename = 'review.csv'

ofile  = open(filename, "w+")

count = 0
with open(filename[:-4] + '.json') as f:
    for l in f:
        count += 1
        line = l.strip()
        json_data = json.loads(line)

        csv_string = []
        for k in json_data.keys()[1:]:
            if not isinstance(json_data[k], unicode):
                csv_string.append(str(json_data[k]))
            else:
                csv_string.append(str(json_data[k].encode('utf-8').decode('ascii', 'ignore')))

        row = ','.join(['"' + str(i).encode('utf-8') + '"' for i in csv_string])
        ofile.write(row.replace('\n', '') + '\n')

        if count == 100:
            sys.exit(0)

ofile.close()

