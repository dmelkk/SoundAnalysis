from scipy.io import wavfile
from pylab import *
import numpy
import sys
import argparse
import dist

file_name = "test.wav"
CHUNK = 2 ** 10
RATE = 44100

def chunk_cut(sound_array):
    for i in numpy.arange(0, len(sound_array)-2*CHUNK, 2*CHUNK):
        a1 = sound_array[i: i + CHUNK]
        a2 = sound_array[i+CHUNK: i + 2*CHUNK]

        s1 = numpy.fft.fft(a1)
        s2 = numpy.fft.fft(a2)

        print "%s\t" % dist.dist(s1, s2)

def get_channels(file_name):
	RATE, sound_array = wavfile.read(file_name)
	channel1 = sound_array[:, 0]
	channel2 = sound_array[:, 1]
	return channel1, channel2

def main():
    ch1, ch2 = get_channels(file_name)
    chunk_cut(ch1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    main()
