#!/usr/bin/python
import sys
import numpy as np
import os
from multiprocessing import Pool
import subprocess
#generate values from -2 to 2, use as input for making files from LangevinDynamics.py


#deltaTs = np.array([0.0000001, 0.000001,0.00001, 0.0001, 0.001,0.01])
trajectoryTs = np.array([0.0001, 0.001, 0.01, 0.1, 0.5, 1])
deltaTs = np.copy(trajectoryTs)#copying is easier than changing code below

threadsToUse = 20
totalRuns = 400
def startRun((j, i)):
   
   value = ["python", "/home/cgoolsby/Documents/gitFolders/langevinDynamics/LangevinDynamics.py", str(j), str(i)]
   output =  "timestep_size_%s/toy.%s"%(i,j)
   f = open(output, "w+")
#   value = ["ls", "-l"]
#   print(i,j, "Print")
   ret = 0
   ret = subprocess.call(value, stdout=f)
   return 1

for f in range(deltaTs.shape[0]):
   os.system("mkdir timestep_size_%s"%deltaTs[f])
   print deltaTs[f]
   runs = np.zeros(totalRuns)
   for i in range(-200, 200, 1):
      j=i/100.0
      runs[i+200] = j

   p = Pool(threadsToUse)
   k=0
   while(k<totalRuns):
      tuples = [(' ', ' ')] * threadsToUse
      k+=threadsToUse
      for l in range(threadsToUse):
          tuples[l] = (runs[k-threadsToUse+l], deltaTs[f])
#      print(p.map(startRun, runs[k-threadsToUse:k], deltaTs[f]))
      print(p.map(startRun, tuples[:]))

#startRun(runs[0], deltaTs[5])
