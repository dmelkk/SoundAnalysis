from scipy.io import wavfile
from pylab import *
import numpy
import sys
import argparse
import dist

file_name = "test.wav"
CHUNK = 2 ** 8
RATE = 44100

def numOfVowels(sound_array):
    res, d = 0, 1
    start = 0
    def finished(t):
        finish = t * 1.0 / (CHUNK * RATE)
        print str(start) + 's to ' + str(finish) + 's'
    a1 = np.zeros(CHUNK)
    s1 = numpy.fft.fft(a1)
    for i in numpy.arange(0, len(sound_array) - CHUNK, CHUNK):
        a2 = sound_array[i: i + CHUNK]
        s2 = numpy.fft.fft(a2)
        d1 = dist.dist(a1, a2)
        a1 = a2
        s1 = s2
        if (i != 0) & (d < 0.1) & (d1 > 0.1):
            finished(i)
            res += 1
        if (d > 0.1) & (d1 < 0.1):
            start = i * 1.0 / (CHUNK * RATE)
        d = d1

    return res

def get_channels(file_name):
	RATE, sound_array = wavfile.read(file_name)
	channel1 = sound_array[:, 0]
	channel2 = sound_array[:, 1]
	return channel1, channel2

def main():
    ch1, ch2 = get_channels(file_name)
    print numOfVowels(ch1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    main()
