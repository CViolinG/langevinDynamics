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
lineNumber = 0
max = 0
for line in file.xreadlines():
    lineNumber +=1
    arr = line.split(", ")
    if(lineNumber==1):
        n=24
        N = np.zeros((n,n))
    for i in range(len(arr)):
        if (i==0):
            print "Line: ", lineNumber
        elif(i==len(arr)-1):
            print "Line End"
        else:
            k, j = int(arr[i]), int(arr[i-1])
#            print k, j
            N[k,j] +=1
            if(int(arr[i])>max):
	        max = int(arr[i])

print max
#print N
f= open("N.txt","w+")
for i in range(N.shape[0]):
    for j in range(N.shape[1]):
        f.write("%d" % N[i,j])
        if(j!=N.shape[1]-1):
            f.write(", ")
    f.write("\n")
f.close()

