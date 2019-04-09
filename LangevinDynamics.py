#!/usr/bin/python
import numpy as np
import math
import random
import sys
deviateAvailable=False

#The purpose of this file is to produce a 1-D langevin dynamics run.
#inputs will be starting coordinates between x and -x
#and F = ma = -gradient (Potential(x)) - dC * velocity * sqrt(2kbtdCT)*R(T)
#where dC is a damping constant, commonly gamma
#and R(T) is the delta correlated stationary gaussian process with zero mean.

#if gamma = 1 we have brownian motion, if =0 we have inertial motion.

def randn(mu, sigma, DA):
        deviateAvailable = DA
        storedDeviate = DA
        #    //        If no deviate has been stored, the polar Box-Muller transformation is
        #//        performed, producing two independent normally-distributed random
        #//        deviates.  One is stored for the next round, and one is returned.
        if not (deviateAvailable):
            
            
#            //        choose pairs of uniformly distributed deviates, discarding those
#                //        that don't fall within the unit circle
            rsquared = 2
            while(rsquared>=1):
                var1=2.0*random.random() - 1.0
                var2=2.0*random.random() - 1.0
                rsquared=var1*var1+var2*var2
            
                
#                //        calculate polar tranformation for each deviate
            polar=math.sqrt(-2.0*math.log(rsquared)/rsquared)
                
#                //        store first deviate and set flag
            storedDeviate=var1*polar
            deviateAvailable=True
                
#                //        return second deviate
            return var2*polar*sigma + mu, storedDeviate
        
#        //        If a deviate is available from a previous call to this function, it is
#        //        returned, and the flag is set to false.
        else:
            deviateAvailable=False
            return storedDeviate*sigma + mu, deviateAvailable



k_ = 0
K = 0
xc = 0
k = 10 
R = 0.001
dt = 0.000001
#dt = float(sys.argv[2])
kb =  0.001987191683
temp = 298
damping = 1
beta = 1 / kb / temp
g = math.sqrt(2/(beta*dt*damping))
dimension = 1
T = 1
#T = float(sys.argv[2])
t=0
x = np.zeros(dimension)
v = np.zeros(dimension)
xa = float(sys.argv[1])

x[0] = float(xa)
while (t<T+dt):
    r2=0
    xa=0
    for i in range(dimension):
        r2+=x[i]*x[i]
        xa+=x[i]/dimension
        
    for i in range(dimension):
#            // defining the potential
#            // U(r)=k/4 (r^2-1)^2 -> -dU/dx=-k(r^2-1)x
#            // Ul(r)=k_ ({x}-({x}.u)u)^2 -> -dU/dx=-k(x-<x>); u=(1/sqrt(N),1/sqrt(N),...); <x>=(x1+x2+...)/N
#            // defining the biasing potential
#            // V(r)=K/2 ({x}-{xc})^2 -> -dV/dx=-K(x-xc)
        randomd, deviateAvailable = randn(0,1,deviateAvailable)
        v[i] = g * randomd - ( k*(r2-1)*x[i] + K*(x[i]-xc) + k_*(x[i]-xa) ) / damping
#        print "Vi, G, Rand, k, r2, xi"
#        print v[i], g, randomd, k, r2, x[i]
#        quit()
        x[i] += dt * v
        if(abs(x[i])>2.16):
             t = T+dt
             continue
        if (R>0):# and (t/dt)%(R/dt)==0):
#            if (i==0):
#                print(t)
            print(t, " ", x[i])
#            if (i==dimension-1):
#                print( "\n")
    t += dt


