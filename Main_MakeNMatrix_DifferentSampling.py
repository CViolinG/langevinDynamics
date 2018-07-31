#!/usr/bin/perl

import numpy as np
import os


sampleFreq = np.array([1, 10, 100, 1000, 10000])
divisors = np.array([1, 2, 4, 8, 16, 32, 64])

for div in divisors:
#  os.system("perl binIt.pl %s copy*/*"%(div))
  fil = 'Output24_%s.txt'%div
  for freq in sampleFreq:
    os.system("python makeNMatrix.py %s %s %s"%(freq, fil, div))
    print freq


