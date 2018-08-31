pusfrom __future__ import division,print_function
from numpy import loadtxt, sqrt
from pylab import plot, show
from random import randint

txt = open("dna.txt")
position_x = [0]
position_y = [0]
flucation = [0]
position_x_r = [0]
position_y_r = [0]


while(1==1):
    char = txt.read(1)
    if not char:
        print("End")
        break
    if(char=='A'):
        position_x.append(position_x[len(position_x)-1] + 1)
        position_y.append(position_y[len(position_y)-1])
    elif(char=='C'):
        position_x.append(position_x[len(position_x)-1] - 1)
        position_y.append(position_y[len(position_y)-1])
    elif(char=='T'):
        position_y.append(position_y[len(position_y)-1] + 1)
        position_x.append(position_x[len(position_x)-1])
    elif(char=='G'):
        position_y.append(position_y[len(position_y)-1] - 1)
        position_x.append(position_x[len(position_x)-1])

    flucation.append(pow((position_x[len(position_x)-2] - position_x[len(position_x)-1]),2) + pow((position_y[len(position_y)-2] - position_y[len(position_y)-1]),2))

    nr = randint(1,4)
    if(nr==1):
        position_x_r.append(position_x_r[len(position_x_r)-1] + 1)
        position_y_r.append(position_y_r[len(position_y_r)-1])
    elif(nr==2):
        position_x_r.append(position_x_r[len(position_x_r)-1] - 1)
        position_y_r.append(position_y_r[len(position_y_r)-1])
    elif(nr==3):
        position_y_r.append(position_y_r[len(position_y_r)-1] + 1)
        position_x_r.append(position_x_r[len(position_x_r)-1])
    else:
        position_y_r.append(position_y_r[len(position_y_r)-1] - 1)
        position_x_r.append(position_x_r[len(position_x_r)-1])
    
plot(position_x, position_y, 'b', position_x_r, position_y_r, 'r')
show()
