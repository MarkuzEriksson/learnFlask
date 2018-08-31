from __future__ import division,print_function
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

# Initial conditions
x = [1]
v = [0]

dt = 0.01

for t in range(0,(int)(20/dt)):
    v.append(v[t]+dt*(-x[t]))
    x.append(x[t] + dt*v[t+1])
    

plot(linspace(0,20,(20+dt)/dt),x)
xlabel('t')
ylabel('x')
show()
