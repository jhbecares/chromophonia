from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
import os
import glob


print os.getcwd()


arrSongs = glob.glob(os.getcwd() + "/../spectrogram/images/*.png")
colors = ("b", "g", "r")

index = {}
images = {}

# loop over the image paths
for i in xrange(1,len(arrSongs)):
    image = cv2.imread(arrSongs[i])
    images[arrSongs[i]] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize, and update
    # the index
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
		        [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist).flatten()
    index[arrSongs[i]] = hist


queryImage = arrSongs[1]

OPENCV_METHODS = (
    ("Correlation", cv2.cv.CV_COMP_CORREL),
    ("Chi-Squared", cv2.cv.CV_COMP_CHISQR),
    ("Intersection", cv2.cv.CV_COMP_INTERSECT), 
    ("Hellinger", cv2.cv.CV_COMP_BHATTACHARYYA))
    
#for i in xrange(1,len(arrSongs)):
#   for j in xrange(i+1,len(arrSongs)):
# loop over the comparison methods
for (methodName, method) in OPENCV_METHODS:
    # initialize the results dictionary and the sort
    # direction
    results = {}
    reverse = False
    
    # if we are using the correlation or intersection
    # method, then sort the results in reverse order
    if methodName in ("Correlation", "Intersection"):
	reverse = True        

    for (k, hist) in index.items():
	# compute the distance between the two histograms
	# using the method and update the results dictionary
	d = cv2.compareHist(index[arrSongs[i]], hist, method)
	results[k] = d
 
    # sort the results
    results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)


    # show the query image
    fig = plt.figure("Query")
    ax = fig.add_subplot(1, 1, 1)
    fulltitle = queryImage.split("/")
    title = fulltitle[len(fulltitle)-1]
    ax.set_title(title)
    ax.imshow(images[queryImage])
    plt.axis("off")
 
    # initialize the results figure
    fig = plt.figure("Results: %s" % (methodName))
    fig.suptitle(methodName, fontsize = 20)
    
    # loop over the results
    count = 1
    countMax = 6
    #plt.subplots_adjust(hspace = 1)
    #fig, axes = plt.subplots(nrows=2, ncols=countMax/2)
    #fig.tight_layout()
    for (i, (v, k)) in enumerate(results):
        if i >= countMax / 2:
            # show the result
	    ax = fig.add_subplot(2, countMax/2, i+1)
            #plt.subplots_adjust(hspace = 1.5)
            sp = k.split("/")
            spcur = sp[len(sp)-1]
	    #ax.set_title("%s: %.2f" % (spcur, v))
            ax.set_title(spcur)
	    plt.imshow(images[k])
	    plt.axis("off")
            count = count + 1
            if count > countMax:
                break
        else:
	    # show the result
	    ax = fig.add_subplot(2, countMax/2, i+1)
            #plt.subplots_adjust(hspace = 1.5)

            sp = k.split("/")
            spcur = sp[len(sp)-1]
	    #ax.set_title("%s: %.2f" % (spcur, v))
            ax.set_title(spcur)
	    plt.imshow(images[k])
	    plt.axis("off")
            count = count + 1
            if count > countMax:
                break

plt.show()
        
# for i in xrange(1,len(arrSongs)):
#     image1 = cv2.imread(arrSongs[i])
#     chans1 = cv2.split(image1)
#     histLen = 1
#     hist2Len = 1
#     hist = {}
#     hist2 = {}
#     for j in xrange(i+1, len(arrSongs)):
#         #os.system('python compare_histograms_1D.py -i "' + arrSongs[i] + '" -i2 "' + arrSongs[j] + '"')
#         image2 = cv2.imread(arrSongs[j])
#         chans2 = cv2.split(image2)

#         for (chan, color) in zip(chans1, colors):
#             hist[histLen] = cv2.calcHist([chan], [0], None, [256], [0,256])
#             histLen = histLen + 1

#         for (chan, color) in zip(chans2, colors):
#             hist2[hist2Len] = cv2.calcHist([chan], [0], None, [256], [0,256])
#             hist2Len = hist2Len + 1
            
#         print "hist1: ", hist
#         print "hist2: ", hist2
