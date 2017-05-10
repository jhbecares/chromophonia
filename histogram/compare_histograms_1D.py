# -*- coding: utf-8 -*-
#     cv2.calcHist(images, channels, mask, histSize, ranges)

#     images: This is the image that we want to compute a histogram
#     for. Wrap it as a list: [myImage].

#     channels: A list of indexes, where we specify the index of the
#     channel we want to compute a histogram for. To compute a
#     histogram of a grayscale image, the list would be [0]. To
#     compute a histogram for all three red, green, and blue channels,
#     the channels list would be [0, 1, 2].

#     mask: I haven’t covered masking yet in this blog yet, but
#     essentially, a mask is a uint8 image with the same shape as our
#     original image, where pixels with a value of zero are ignored
#     and pixels with a value greater than zero are included in the
#     histogram computation. Using masks allow us to only compute a
#     histogram for a particular region of an image. For now, we’ll
#     just use a value of None for the mask.

#     histSize: This is the number of bins we want to use when
#     computing a histogram. Again, this is a list, one for each
#     channel we are computing a histogram for. The bin sizes do not
#     all have to be the same. Here is an example of 32 bins for each
#     channel: [32, 32, 32].

#     ranges: The range of possible pixel values. Normally, this is
#     [0, 256] for each channel, but if you are using a color space
#     other than RGB (such as HSV), the ranges might be different.



# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-i", "--image", required = True, help = "Path to the first image")
ap.add_argument("-i2", "--image2", required = True, help = "Path to the second image")

args = vars(ap.parse_args())

fig = plt.figure()
a = fig.add_subplot(1,2,1)
b = fig.add_subplot(1,2,2)

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("image", image)


# grab the image channels, initialize the tuple of colors,
# the figure and the flattened feature vector
chans = cv2.split(image)
colors = ("b", "g", "r") # Cuidado con el orden! esta cambiado en opencv
#a.figure()
a.set_title("'Flattened' Color Histogram")
a.set_xlabel("Bins")
a.set_ylabel("# of Pixels")
features = []
 
# loop over the image channels
for (chan, color) in zip(chans, colors):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist)
 
	# plot the histogram
	a.plot(hist, color = color)
	a.set_xlim([0, 256])
 
# here we are simply showing the dimensionality of the
# flattened color histogram 256 bins for each channel
# x 3 channels = 768 total values -- in practice, we would
# normally not use 256 bins for each channel, a choice
# between 32-96 bins are normally used, but this tends
# to be application dependent
print "flattened feature vector size: %d" % (np.array(features).flatten().shape)
plt.show(block=False)



image2 = cv2.imread(args["image2"])
cv2.imshow("image2", image2)
chans2 = cv2.split(image2)
colors2 = ("b", "g", "r") # Cuidado con el orden! esta cambiado en opencv
#b.figure()
b.set_title("'Flattened' Color Histogram")
b.set_xlabel("Bins")
b.set_ylabel("# of Pixels")
features = []
for (chan, color) in zip(chans2, colors2):
	# create a histogram for the current channel and
	# concatenate the resulting histograms for each
	# channel
	hist2 = cv2.calcHist([chan], [0], None, [256], [0, 256])
	features.extend(hist2)
 
	# plot the histogram
	b.plot(hist2, color = color) 
	b.set_xlim([0, 256])


plt.show(block=False)


# Not all scores are bounded:

# CV_COMP_CORREL: [-1;1] where 1 is perfect match and -1 is the worst.
# CV_COMP_CHISQR: [0;+infinty] where 0 is perfect match and mismatch
# is unbounded (see doc for equation of comparison) CV_COMP_INTERSECT:
# [0;1] (if histograms are normalized) where 1 is perfect match and 0
# mismatch.  CV_COMP_BHATTACHARYYA and CV_COMP_HELLINGER: [0;1] where
# 0 is perfect match and 1 mismatch.  Equations of methods are
# here. An explaination with schema is available in ''Learning OpenCV
# Computer Vision with OpenCV Library, from G. Bradski and
# A. Kaehler'' p. 203.  print "La super distancia: ",

# print "La super distancia con CV_COMP_CORREL: [-1;1] where 1 is perfect match and -1 is the worst.: ", cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_CORREL)
# print "La super distancia CV_COMP_CHISQR: [0;+infinty] where 0 is perfect match and mismatch is unbounded: ", cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_CHISQR)
# print "La super distancia CV_COMP_INTERSECT: ", cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_INTERSECT)
# print "La super distancia CV_COMP_BHATTACHARYYA (0 to 1, where 0 is perfect match and 1 is mismatch): ", cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_BHATTACHARYYA)


print  cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_CORREL)
print  cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_CHISQR)
print  cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_INTERSECT)
print  cv2.compareHist(hist, hist2, cv2.cv.CV_COMP_BHATTACHARYYA)
