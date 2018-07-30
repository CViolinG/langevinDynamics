#!/usr/bin/perl

import numpy as np
import os


sampleFreq = np.array([1, 10, 100, 1000, 10000])

for freq in sampleFreq:
   os.system("python %s makeNMatrix.py %s"%(freq,freq))
   print freq


