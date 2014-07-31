#-------------------------------------------------------------------------------
# Name:        j2db
# Purpose:     business.json to database
#
# Author:      Animesh Pandey
#
# Created:     10/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import json
import sys
from pprint import pprint
import MySQLdb as mdb

##count = 0

try:
    con = mdb.connect('localhost', 'root', 'root', 'yelp');
    with con:
        cur = con.cursor()
        with open('business.json') as f:
            for l in f:
##                count += 1
                line = l.strip()
                json_data = json.loads(line)

                str1  = json.dumps(json_data['business_id'])
                str2  = json.dumps(json_data['name'])
                str3  = json.dumps(json_data['full_address'])
                str4  = json.dumps(json_data['city'])
                str5  = json.dumps(json_data['state'])
                str6  = str(json_data['latitude']    )
                str7  = str(json_data['longitude']   )
                str8  = str(json_data['stars']       )
                str9  = str(json_data['review_count'])
                str10 = str(json_data['open']        )
                if len(json_data['neighborhoods']) == 0:
                    str11 = "NULL"
                else:
                    str11 = ','.join(json_data['neighborhoods'])

##                print json_data['neighborhoods']

                query = 'INSERT INTO business VALUES ("' + str1[1:-1] + '", "'+ str2[1:-1]+ '", "' + str3[1:-1] + '", "' + str4[1:-1] + '", "' + str5[1:-1] + '", ' + str6 + ', ' + str7 + ', ' + str8 + ', ' + str9 + ', ' + str10 + ', ' + str11 + ')'

##                print query

                cur.execute(query)
                con.commit()

##                if count == 2:
##                    sys.exit(0)

except mdb.Error, e:
    print query
    print e
    sys.exit(1)

finally:
    if con:
        con.close()
