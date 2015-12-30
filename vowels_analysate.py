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
    res, d = 0, 0
    for i in numpy.arange(0, len(sound_array)-2*CHUNK, 2*CHUNK):
        a1 = sound_array[i: i + CHUNK]
        a2 = sound_array[i+CHUNK: i + 2*CHUNK]

        s1 = numpy.fft.fft(a1)
        s2 = numpy.fft.fft(a2)
        d1 = dist.dist(a1, a2)
        if (i != 0) & (d < 0.1) & (d1 > 0.1):
            res += 1
        d = d1
        print d
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
