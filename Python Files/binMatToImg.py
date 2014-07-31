#-------------------------------------------------------------------------------
# Name:        Binary Matrix to Image
# Purpose:     Read from a csv or from any flat-file and convert the binary
#              matrix to a monochrome image. (For representation purposes)
#
# Author:      Animesh Pandey
#
# Created:     05/07/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import csv
import PIL.ImageOps as pi
from PIL import Image
import numpy as np
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist, cosine, jaccard, squareform
from matplotlib.mlab import PCA
import random
import matplotlib.pyplot as plt

image_mat = []
with open('yelp.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        image_mat.append([int(i) for i in row])
##        image_mat.append(list([i+2 for i in np.bitwise_not(np.asarray([int(i) for i in row]))]))

image_mat = np.asarray(image_mat)

im = Image.fromarray(image_mat*255)
im.show()

##distances = pdist(image_mat, jaccard)
##distances_2d = squareform(distances)
