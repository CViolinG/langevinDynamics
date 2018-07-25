#!/usr/bin/python
import sys
import numpy as np
import os
from multiprocessing import Pool
import subprocess
#generate values from -2 to 2, use as input for making files from LangevinDynamics.py


#deltaTs = np.array([0.0000001, 0.000001,0.00001, 0.0001, 0.001,0.01])
#trajectoryTs = np.array([0.0001, 0.001, 0.01, 0.1, 0.5, 1])
copies = np.arange(25)
copies = copies 
deltaTs = np.copy(copies)#copying is easier than changing code below
a = np.zeros(24)
a[0] = -2.0
xRange = 4.0
for i in range(a.shape[0]):
   a[i] += a[i-1] + 1.0 / (a.shape[0] / xRange)

startingPoints = np.zeros(24)
for i in range(a.shape[0] - 1):
   startingPoints[i] = (a[i] + a[i+1])/2.0
startingPoints[startingPoints.shape[0]-1] = -1.0 * startingPoints[startingPoints.shape[0]-2]
print startingPoints
threadsToUse = 24
totalRuns = 24  
def startRun((j, i)):
   value = ["python", "./LangevinDynamics.py", str(j)]#, str(i)]
   output =  "copy_%s/toy.%s"%(i,j)
   print "Printing to %s"%output
   f = open(output, "w+")
#   value = ["ls", "-l"]
#   print(i,j, "Print")
   ret = 0
   ret = subprocess.call(value, stdout=f)
   return 1

for f in range(deltaTs.shape[0]):
   os.system("mkdir copy_%s"%deltaTs[f])
   print deltaTs[f]
   runs = np.zeros(totalRuns)
   for i in range(24):
      j=startingPoints[i]
      runs[i] = j

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
