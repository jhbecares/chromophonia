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



nsamples = 128

rangesample = int(bins.size/nsamples)

excess = ((bins.size % nsamples) != 0)

print("Capturando el audio de ",bins.size," en ",nsamples," de tamaño ",rangesample)

for steps in range(0,nsamples):

    maxfreq = 0

    if( (steps+1 == nsamples) and excess):
        n_steps = rangesample +  (bins.size % nsamples)
    else:
        n_steps = rangesample

    for step_columns in range(0,n_steps):
        index = step_columns + steps

        maxfreq = spectrogram_data[0][index]

        for step_frequency in range(0, freqs.size-1):
            if step_frequency > 100 and step_frequency < 400:
                if spectrogram_data[step_frequency][index] >= maxfreq:
                    maxfreq = step_frequency

    aux_array = []
    norm = maxfreq/(freqs.size-1)
    deg = 360 * norm
    col = hsv_to_rgb((deg,1,1))

    for h in range(0,nsamples):
        aux_array.append(col)
    final_values.append(aux_array)


from pylab import imshow, show, get_cmap

plt.imshow(final_values)
plt.show()