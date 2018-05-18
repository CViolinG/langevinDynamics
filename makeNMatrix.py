#!/usr/bin/python
import numpy as np

#while(<>){
#    @split = split /,/;
#        foreach $value (@split){
#            $array[$value][$ +=1;
#                           }
#                           }$i=0;
#                           foreach (@array){
#                           $i+=1;
#                           print "$i, $_\n";
#                           }
#


file = open("Output24.txt")
N = np.zeros((24,24))
lineNumber = 0
for line in file.xreadlines():
    lineNumber +=1
    arr = line.split(", ")
    for i in range(len(arr)):
        if (i==0):
            print "Line: ", lineNumber
        elif(i==len(arr)-1):
            print "Line End"
        else:
            k, j = int(arr[i]), int(arr[i-1])
#            print k, j
            N[k,j] +=1

print N
f= open("N.txt","w+")
for i in range(N.shape[0]):
    for j in range(N.shape[1]):
        f.write("%d, " % N[i,j])
    f.write("\n")
f.close()

