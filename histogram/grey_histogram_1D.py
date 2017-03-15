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
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
 
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("image", image)

# convert the image to grayscale and create a histogram
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
print 'fin'
