import numpy as np
from classes import *

def CreateYbus(list_lines, list_buses):

    Y = np.zeros((len(list_buses),len(list_buses)) , dtype = complex)
    for i in list_lines:
        Y[i.a-1,i.a-1] += i.y[0,0]
        Y[i.b-1,i.b-1] += i.y[1,1]
        Y[i.a-1,i.b-1] += i.y[0,1]
        Y[i.b-1,i.a-1] += i.y[1,0]

    return Y


L1 = line(1,2,0.2j)
L2 = line(2,3,0.1j)

buses = [1,2,3]

Y_bus = CreateYbus(list_lines, buses)

print(Y_bus)