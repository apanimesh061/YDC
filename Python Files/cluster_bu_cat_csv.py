#-------------------------------------------------------------------------------
# Name:        cluster_bu_cat_csv
# Purpose:     Database exported to CSV in order to save time lost in reading DB
#
# Author:      Animesh Pandey
#
# Created:     17/04/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import csv, sys
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
import mdp
from scipy.spatial.distance import pdist, cosine, squareform
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

count = 0
with open('yelp.csv', 'rb') as f:
    reader = csv.reader(f)
    A = []
    for row in reader:
        count += 1
        A.append([float(x) for x in row])
##        if count == 10:
##            B = np.asarray(A)
##            sys.exit(1)
f.close()

B = np.asarray(A)
pca = PCA(n_components=2).fit_transform(B)

db = DBSCAN(eps=0.1, min_samples=3).fit(pca)
core_samples = db.core_sample_indices_
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(B, labels))
