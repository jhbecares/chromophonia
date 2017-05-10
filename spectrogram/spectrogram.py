import matplotlib
matplotlib.use('Qt5Agg')
import re
from scipy.io import wavfile
import numpy as np
from matplotlib.colors import hsv_to_rgb
import argparse
from heapq import *

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-f", "--file", required=False, help="Path to the file")
args = vars(ap.parse_args())

# Grab your wav and filter it
file = 'wavs/00/samp2.wav'
if (args["file"]):
    file = str(args["file"])
filename = re.match( r'.*\/(.*?)\.wav', file, re.M|re.I).group(1)
output = 'images/'+filename+'.png'
print('Generating ',file,' chromoponia tag in ',output)
rate, data2 = wavfile.read(file)
#data = []
print('Merging stereo data...')
#for x in data2:
#    data.append(np.mean(x))
print(len(data2))
try:
    data = (data2[:,0] + data2[:,1]) / 2
except:
    data = data2
print('Stereo data merged...')

from matplotlib import pyplot as plt
from matplotlib.pyplot import specgram

spectrogram_data, freqs, bins, im = specgram(data, NFFT=1024, Fs=rate)

final_values = []

print('Spectrogram created... ')

nsamples = 128

rangesample = int(bins.size/nsamples)

excess = ((bins.size % nsamples) != 0)

print("Creating slices of size ",bins.size," in ",nsamples," samples with size of ",rangesample)

for steps in range(0,nsamples):

    maxfreq = 0

    if( (steps+1 == nsamples) and excess):
        n_steps = rangesample +  (bins.size % nsamples)
    else:
        n_steps = rangesample
    h = []
    for step_columns in range(0,n_steps):
        index = step_columns + steps

        maxfreq = spectrogram_data[0][index]

        for step_frequency in range(0, freqs.size-1):
            if step_frequency > 3 and step_frequency < 513:
                #if spectrogram_data[step_frequency][index] >= maxfreq:
                #    maxfreq = step_frequency
                heappush(h, (spectrogram_data[step_frequency][index],step_frequency))

    aux_array = []
    largest = nlargest(40,h)
    largestfreqs = []
    for k,v in largest:
        largestfreqs.append(pow(v,4))
    maxfreq = np.mean(largestfreqs)
    #norm = maxfreq/(freqs.size-1)
    deg = (((pow(maxfreq,2)) % 350)+10.0)/360;
    #print(deg)
    col = hsv_to_rgb((deg,1.0,1.0))

    for h in range(0,nsamples):
        aux_array.append(col)
    final_values.append(aux_array)


from pylab import imshow, show, get_cmap

plt.imshow(final_values)
plt.axis('off')
plt.savefig(output,bbox_inches='tight')