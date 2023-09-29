import cmath, math
import numpy as np

list_lines = [] #list of all instances of lines 
list_buses = [] #list of all instances of bus
PQPV = [] #each element in the list is a number that is either a PQ or PV bus, length is number of PQPV buses
PQ = [] #each element in the list is a number that is a PQ bus, length is number of PQ buses


class line:
    def __init__(self, a, b, zab):
        #a is bus number from
        #b is bus number to
        #zab is impedance on line a-b

        self.a = a
        self.b = b
        
        yab = 1/zab
        self.y = np.array([[yab, -yab], [-yab, yab]])

        list_lines.append(self)

class bus:
    def __init__(self, a, Va, da, Pa, Qa, type):
        #a is bus number
        #Va is voltage magnitude
        #da is voltage angle
        #Pa is bus real power
        #Qa is reactive power
        #type is a string that is either: slack, PV or PQ

        self.a = a
        self.Va = Va
        self.da = da
        self.Pa = Pa
        self.Qa = Qa
        self.type = type

        if type != 'slack':
            PQPV.append(a-1)
        if type == 'PQ':
            PQ.append(a-1)

        list_buses.append(self)