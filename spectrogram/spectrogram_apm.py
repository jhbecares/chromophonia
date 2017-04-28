import matplotlib
matplotlib.use('Qt5Agg')

from scipy.io import wavfile
import numpy as np
from matplotlib.colors import hsv_to_rgb

# Grab your wav and filter it
mywav = 'sample.wav'
rate, data2 = wavfile.read(mywav)
data = []

for x in data2:
    data.append(np.mean(x))


from matplotlib import pyplot as plt
from matplotlib.pyplot import specgram

spectrogram_data, freqs, bins, im = specgram(data, NFFT=1024, Fs=rate)

final_values = []
maxamp = 0
for cols in spectrogram_data:
    for rows in cols:
        if maxamp < rows:
            maxamp = rows
print("Máxima amplitud: ",maxamp)
print("Nº de frecuencias capturadas: ",freqs.size)
nsamples = 128

rangesample = int(bins.size/nsamples)

excess = ((bins.size % nsamples) != 0)

print("Capturando el audio de ",bins.size," en ",nsamples," de tamaño ",rangesample)
check = 0
for steps in range(0,nsamples):

    maxfreq = 0

    if( (steps+1 == nsamples) and excess):
        n_steps = rangesample +  (bins.size % nsamples)
    else:
        n_steps = rangesample
    aux_array = []
    for step_columns in range(0,n_steps):
        index = step_columns + steps

        maxfreq = spectrogram_data[0][index]
        actual_frecuency = 0
        for current_amplitude_frequency in range(0, freqs.size):

            norm = actual_frecuency / (freqs.size - 1)
            deg = 360 * norm
            amp = np.log(current_amplitude_frequency) / np.log(maxamp)

            if amp < 0.001:
                amp = 0
            print(actual_frecuency)
            col = hsv_to_rgb((deg, amp, amp))
            #print (col)
            aux_array.append(col)
            actual_frecuency +=1;

    final_values.append(aux_array)
    if(check == 50):
        plt.imshow(final_values, cmap="hsv")
        plt.show()
        check = 0
    check += 1

from pylab import imshow, show, get_cmap

plt.imshow(final_values,cmap="hsv")
plt.show()