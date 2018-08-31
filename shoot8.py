from __future__ import division,print_function
from numpy import linspace, tan, cos, pi, sin
from pylab import plot, show, xlabel, ylabel

# Example task 13 in Computitational Phyrics
# By Markus Eriksson
# Phyton v2.7.5

# This program calculates the ballistic trajectory using the Leap-Frog method

# Constants
t = 30
V = 1000/3.6;
G = 10;
dt = 0.01

# Initials 
x_lp = [0]
y_lp = [0]
vx_lp = [V*cos(t*pi/180.0)]
vy_lp = [V*sin(t*pi/180.0)-(dt/2)*G]

# Shoot7. Calcultaing trajectory using analytical solution
x = linspace(1,2*tan(t*pi/180.0)*V*V*cos(t*pi/180.0)*cos(t*pi/180.0)/G, 1000);
y = x*tan(t*pi/180) - 0.5*G*x*x/(V*V*cos(t*pi/180.0)*cos(t*pi/180.0));

# Shoot8. Calculating trajectory using Leap-Frog method
for n in range(0,10000):
    x_lp.append(x_lp[n] + dt*vx_lp[n])
    vx_lp.append(vx_lp[n])
    y_lp.append(y_lp[n] + dt*vy_lp[n])
    vy_lp.append(vy_lp[n] - dt*G)
    if(y_lp[n+1]<0):
        x_lp.pop()
        y_lp.pop()
        vx_lp.pop()
        vy_lp.pop()
        asdasd
        break;

# Plot Shoot 7 vs Shoot 8
xlabel("x [m]")
ylabel("y [m]")
plot(x_lp,y_lp,"+b")
plot(x,y,"r")
show()
