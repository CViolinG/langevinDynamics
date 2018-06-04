#!/usr/bin/python
import sys
import numpy as np
import os
from multiprocessing import Pool
import subprocess
#generate values from -2 to 2, use as input for making files from LangevinDynamics.py

threadsToUse = 20
totalRuns = 400
def startRun(j):
   value = ["python", "/home/cgoolsby/Documents/gitFolders/langevinDynamics/LangevinDynamics.py", str(j)]
   output =  "biharmonic/toy.%s"%j
   f = open(output, "w+")
#   value = ["ls", "-l"]
   print(j)
   ret = 0
   ret = subprocess.call(value, stdout=f)
   return 1

runs = np.zeros(totalRuns)
for i in range(-200, 200, 1):
   j=i/100.0
   runs[i+200] = j

p = Pool(threadsToUse)
k=0
while(k<totalRuns):
   k+=threadsToUse
   print(p.map(startRun, runs[k-threadsToUse:k]))
