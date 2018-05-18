#!/usr/bin/python
import sys
import os
#generate values from -2 to 2, use as input for making files from LangevinDynamics.py


for i in range(-20, 20, 1):
	j =i/10.0
	print j
	value = "python LangevinDynamics.py %s > toy.%s" % (j, j)
	os.system(value)
	
