#-------------------------------------------------------------------------------
# Name:        cluster_bu_cat
# Purpose:     cluster businesses on the basis of cosine similarity
#
# Author:      Animesh Pandey
#
# Created:     13/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import numpy as np
import mdp
from scipy.cluster import hierarchy
import MySQLdb as mdb
from scipy.spatial.distance import pdist, cosine, squareform
from matplotlib.mlab import PCA
import random
import matplotlib.pyplot as plt

try:
    con = mdb.connect('localhost', 'root', 'root', 'yelp');
    con.query('SET GLOBAL connect_timeout=288000')
    con.query('SET GLOBAL wait_timeout=288000')
    con.query('SET GLOBAL interactive_timeout=288000')
    with con:
        cur = con.cursor()
        cur.execute("select * from bu_cat")
        rows = cur.fetchall()
        A = rows[0]
        for row in rows[1:]:
            A = np.vstack([A, list(row)])

except mdb.Error, e:
    print e
    sys.exit(1)

finally:
    if con:
        con.close()

A = mdp.pca(A.astype('float32'), reduce=True)

##distances = pdist(A, cosine)
##distances_2d = squareform(distances)
clusters = hierarchy.linkage(A, method='complete', metric='cosine')
flat_clusters = hierarchy.fcluster(clusters.clip(0,100000), 0.8,'inconsistent')
plt.scatter(*numpy.transpose(A), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
with open('Clusters.dat', 'w+') as f:
    count = 0
    for v in flat_clusters:
        count += 1
        f.write(str(count) + "\t" + str(v) + "\n")
f.close()

