from scipy.io import wavfile
from pylab import *
import numpy
import sys
import argparse

CHUNK = 2 ** 10
RATE = 44100

def chunk_cut(sound_array):
    for i in numpy.arange(0, len(sound_array)-2*CHUNK, 2*CHUNK):
        a1 = sound_array[i: i + CHUNK]
        a2 = sound_array[i+CHUNK: i + 2*CHUNK]

        s1 = numpy.fft.fft(a1)
        s2 = numpy.fft.fft(a2)

        print "%s\t" % dist(s1, s2)
