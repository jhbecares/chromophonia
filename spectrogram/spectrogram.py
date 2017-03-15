import matplotlib
matplotlib.use('Qt5Agg')

from scipy.io import wavfile
import numpy as np
# Grab your wav and filter it
mywav = 'samp2.wav'
rate, data2 = wavfile.read(mywav)
data = []
for x in data2:
    data.append(np.mean(x))


from matplotlib import pyplot as plt
from matplotlib.pyplot import specgram

Pxx, freqs, bins, im = plt.specgram(data, NFFT=1024,Fs=rate,scale_by_freq=False)

plt.show()
final_values = []

nsamples = 128

rangesample = int(bins.size/nsamples)

excess = bins.size % nsamples == 0

print("Capturando el audio de ",bins.size," en ",nsamples," de tamaño ",rangesample)

for val in Pxx:
    print(val[0])

for steps in range(0,nsamples-1):

    maxfreq = 0

    if( steps == nsamples - 1 and excess):
        n_steps = rangesample +  bins.size % nsamples
    else:
        n_steps = rangesample

    for step_columns in range(0,n_steps-1):

        index = step_columns + steps

        maxfreq = Pxx[0][index]

        for n in range(0,freqs.size-1):

            if Pxx[n][index] >= maxfreq:
                maxfreq = n

    aux_array = []
    for h in range(0,nsamples-1):
        aux_array.append(maxfreq/freqs.size-1)
    final_values.append(aux_array)

print(freqs)
from pylab import imshow, show, get_cmap
print(freqs.size)
imshow(final_values, cmap=get_cmap("Spectral"), interpolation='nearest')
show()