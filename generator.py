#!/usr/bin/python
import sys
import numpy as np
import os
from multiprocessing import Pool
import subprocess
#generate values from -2 to 2, use as input for making files from LangevinDynamics.py


#deltaTs = np.array([0.0000001, 0.000001,0.00001, 0.0001, 0.001,0.01])
#trajectoryTs = np.array([0.0001, 0.001, 0.01, 0.1, 0.5, 1])
copies = np.arange(100)
copies = copies 
deltaTs = np.copy(copies)#copying is easier than changing code below
a = np.zeros(25)
xRange = 4.0
a[0] = -2.0 - 1.0/ ((a.shape[0]-1) / xRange)
for i in range(a.shape[0]):
   a[i] += a[i-1] + 1.0 / ((a.shape[0]-1) / xRange)
startingPoints = np.zeros(24)
for i in range(a.shape[0] - 1):
   startingPoints[i] = (a[i] + a[i+1])/2.0
print(startingPoints)
threadsToUse = 24
totalRuns = 24

def startRun(i, j):
   value = ["python3", "./LangevinDynamics.py", str(j)]#, str(i)]
   output =  "copy_{}/toy.{}".format(i,j)
   print("Printing to {}".format(output))
   os.system("python3 LangevinDynamics.py {} > {} &".format(j, output))
   return 1

for i in range(totalRuns):
    os.system("mkdir copy_{}".format(i))
    for j in startingPoints:
        print(i, j)
        startRun(i, j)
#        value = ["python3", "./LangevinDynamics.py", str(j)]
#        output = "copy_{}/toy_{}".format(i,j)
#        f = open(output, "w")
#        ret = subprocess.call(value, stdout=f)

    
quit()

def startRun(i, j):
   value = ["python3", "./LangevinDynamics.py", str(j)]#, str(i)]
   output =  "copy_%s/toy.%s"%(i,j)
   print("Printing to {}".format(output))
   f = open(output, "w+")
   ret = subprocess.call(value, stdout=f)
   return 1

for f in range(deltaTs.shape[0]):
   os.system("mkdir copy_%s"%deltaTs[f])
   print(deltaTs[f])
   runs = np.zeros(totalRuns)
   for i in range(a.shape[0]-1):
      j=startingPoints[i]
      runs[i] = j

   p = Pool(threadsToUse)
   k=0
   while(k<totalRuns):
      tuples = [(' ', ' ')] * threadsToUse
      print("k: {}".format(k))
      k+=threadsToUse
      for l in range(threadsToUse):
      #    tuples[l] = (runs[k-threadsToUse+l], deltaTs[f])
        startRun(deltaTs[f], runs[k-threadsToUse+l])
#      print(p.map(startRun, runs[k-threadsToUse:k], deltaTs[f]))
      
#startRun(runs[0], deltaTs[5])

#os.system("perl binIt.pl 1 copy*/*")
#os.system("python makeNMatrix.py 1 Output40_1.txt t")
