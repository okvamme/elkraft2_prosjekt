import math

def P_calculated(bus, list_buses, Y_bus):
    #bus is the specific bus you are calculating P for
    #list_buses is a list of all instances of the class bus
    #Y_bus is the Ybus for the system

    P_calc = 0
    for b in list_buses:
        P_calc += bus.Va * b.Va * (Y_bus[bus.a - 1, b.a - 1].real * math.cos(bus.da - b.da) + Y_bus[bus.a - 1, b.a - 1].imag *math.sin(bus.da - b.da))
    
    return P_calc

def Q_calculated(bus, list_buses, Y_bus):
    #bus is the specific bus you are calculating Q for
    #list_buses is a list of all instances of the class bus
    #Y_bus is the Ybus for the system

    Q_calc = 0
    for b in list_buses:
        Q_calc += bus.Va * b.Va * (Y_bus[bus.a - 1 , b.a - 1].real * math.sin(bus.da - b.da) - Y_bus[bus.a - 1 , b.a - 1].imag *math.cos(bus.da - b.da))
    
    return Q_calc
