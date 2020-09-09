#!/usr/bin/python
import random as r
import math as m

# Loop over a bunch of Monte Carlo trials
counter=0
Nsteps=100000000
for i in range(Nsteps):
    x=r.uniform(-1.,1.)
    y=r.uniform(-1.,1.)

    # Test if the random x,y point is in the unit circle
    if x*x+y*y < 1:
        counter +=1

    # Every so often, print out our current estimate
    if ((i+1)%10000==0):
        pi_estimate = float(counter)*4./float(i+1)
        print("{0} {1}".format(str(i),str(pi_estimate)))
