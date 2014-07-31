#-------------------------------------------------------------------------------
# Name:        yelpJsonReader
# Purpose:     Read the file provided by Yelp
#
# Author:      Animesh Pandey
#
# Created:     05/03/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import json
import sys
import re
import os

filename = "./yelp_phoenix_academic_dataset/DataSet"

progBusiness = re.compile(r'({"business_id":(\s\S*)*"type":(\s\S*)*})')
progCheckin  = re.compile(r'({"checkin_info":(\s\S*)*"business_id":(\s\S*)*})')
progVotes    = re.compile(r'({"votes":(\s\S*)*"business_id":(\s\S*)*})')
progUsers    = re.compile(r'({"user_id":(\s\S*)*"type":(\s\S*)*})')
progYelp     = re.compile(r'({"yelping_since":(\s\S*)*"elite":(\s\S*)*})')

file1 = open('business.json', 'w+')
file2 = open('checkin.json' , 'w+')
file3 = open('review.json'  , 'w+')
file4 = open('users.json'   , 'w+')
file5 = open('tip.json'     , 'w+')
file6 = open('other.json'   , 'w+')

data = []
count = 0
with open(filename) as f:
    for l in f:
        line = l.lstrip()
        count = count + 1
        data.append(line)

        if progBusiness.match(line):
            file1.write(line)

        elif progCheckin.match(line):
            file2.write(line)

        elif progVotes.match(line):
            file3.write(line)

        elif progUsers.match(line):
            file4.write(line)

        elif progYelp.match(line):
            file5.write(line)

        else:
            file6.write(line)

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
