import random
import math
import numpy

def sq(x):
    return x*x

# Let gamma be the orientation angle of the triange, between 0 and 2pi.
# 0 indicates the point is facing the oncoming projectile
# pi indicates that it is facing in the same direction as the projectile

# Function to determine the intersect point between y=b and the line between two points
def impact(point1,point2,b):
    slope=(point2[1]-point1[1])/(point2[0]-point1[0])
    hits=(((b<point1[1])and(b>point2[1])) or ((b>point1[1])and(b<point2[1]))) # Tests if the impact parameter is in between the points
    x_impact=(b-point1[1])/slope + point1[0] # Intersect of edge line and y=b
    theta=2.*math.atan(slope)
    return hits, x_impact, theta

# Function to determine the scattering angle from a list of the triangle's corners and impact parameter
def scattering_angle(corners,b):
    theta=0.
    x=1000

    # Test all three edges
    this_hit, this_impact, this_theta=impact(corners[0],corners[1],b)
    if (this_hit) and (this_impact < x):
        x=this_impact
        theta=this_theta
    this_hit, this_impact, this_theta=impact(corners[0],corners[2],b)
    if (this_hit) and (this_impact < x):
        x=this_impact
        theta=this_theta
    this_hit, this_impact, this_theta=impact(corners[2],corners[1],b)
    if (this_hit) and (this_impact < x):
        x=this_impact
        theta=this_theta

    return theta

side=1
bases=[0.5,1.0,1.5]
hists=[]

for base in bases:
    # Let beta be half the angle formed by point 0
    beta=math.asin(0.5*base/side)

    # The distances to each corner
    dists=[2./3.*side*math.cos(beta),math.sqrt(sq(0.5*base) + sq(1./3.*side*math.cos(beta))),math.sqrt(sq(0.5*base) + sq(1./3.*side*math.cos(beta)))]
    max_dist=max(dists)
    
    # The angles to each corner
    angles=[0,math.pi-math.asin(0.5*base/dists[1]),math.pi+math.asin(0.5*base/dists[1])]

    # Do the Monte Carlo
    N_scatters=1000000
    thetas=[]
    for i in range(N_scatters):
        
        # Generate a random orientation and a random impact parameter
        gamma=2.*math.pi*random.random()
        b=2.*max_dist*(random.random()-0.5) # Pick an impact parameter from +/- the max possible
        
        # Determine the coordinates of the three corners of the triangle for the given orientation.
        corners=[]
        for j in range(3):
            corners.append([dists[j]*math.cos(gamma+angles[j]),dists[j]*math.sin(gamma+angles[j])])
            
        theta=scattering_angle(corners,b)
        if (theta!=0.):
            thetas.append(theta*180/math.pi)

    hist,edges=numpy.histogram(thetas,bins=90,range=(-180.,180.),weights=2.*max_dist/float(N_scatters)/4.*numpy.ones_like(thetas))
    hists.append(hist)
            
for i in range(90):
    print(-179+4.*i,end=' ')
    for hist in hists:
        print(hist[i],end=' ')
    print('')


