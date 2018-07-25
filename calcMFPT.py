#!/usr/bin/python
import sys
#quite simple, calculate the Mean First Passage Time from -1.0 to 1.0.
#read in output files, then grab any value of -1.0 or 1.0
#keep track of steps until the other one is seen.

MFTP = []
MFTP.append([])
MFTP.append([])
for i in range(len(sys.argv)-1):
  file = open(sys.argv[i+1])
  for line in file.xreadlines():
    start = 0
    ar = line.split(", ")
    time = 0
    current = 100
    if(len(ar)>2):
      for j in range(len(ar)):
        if(ar[j]=='\n'):
          ar[j] = 1000
        if((int(ar[j]) == -1 or int(ar[j]) == 1) and time == 0):
          start = 1
          current = int(ar[j])
          time = 1
        if(start == 1 and int(ar[j]) != -1 * current):
          time += 1
        if(int(ar[j]) == -1 * current):
          MFTP[current%3%2].append(time-1)#current%3%2 gives 0 or 1 for -1 or 1 respectively
          time = 2 
          current = int(ar[j])

  print MFTP[0]
  print
  print MFTP[1]
        
      
