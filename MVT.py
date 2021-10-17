import numpy as np
import matplotlib.pyplot as plt 
from math import *

# Constants
l=900           #mm
b=87            #mm
h=150           #mm
e=3             #mm
O=(b-e)*(h-e)   #mm2
I=(e * (h**3))/6 + 0.5*e*(b-e)*(h-e)*(h-e) #mm4
P=400           #N


def M(x3):
    if 0 <=x3<(l/3):
        return P*x3
    elif (l/3)< x3 <((2*l)/3):
        return ((-P/2)*(x3-(l/3)))+((P*l)/2) 
    elif ((2*l)/3)< x3 <=l :
        return (((-3)*P*(x3-((2*l)/3)))/2)+((P*l)/3) 
    else :
        return 0

M_x=[]
M_y=[]
for j in range(0,l,1):
    M_x.append(j)
    M_y.append(M(j)) 
plt.figure(1)
diagrame_m = plt.plot(M_x, M_y)

def T(x3):
    if 0 <=x3<(l/3):
        return 0
    elif (l/3)< x3 <=((2*l)/3):
        return ((1/0.364)*P*l)/6 
    elif ((2*l)/3)<= x3 <=l :
        return ((1/0.364)*P*l)/6 
    else:
        return 0

T_x=[]
T_y=[]
for j in range(0,l,1):
    T_x.append(j)
    T_y.append(T(j)) 
plt.figure(2)
diagrame_v = plt.plot(T_x, T_y)
    
def V(x3):
    if 0 <=x3<(l/3):
        return P
    elif (l/3)< x3 <=((2*l)/3):
        return -P/2
    elif ((2*l)/3)<= x3 <=l:
        return-3*P/2 
    else:
        return 0

V_x=[]
V_y=[]
for j in range(0,l,1):
    V_x.append(j)
    V_y.append(V(j)) 
plt.figure(3)
diagrame_V = plt.plot(V_x, V_y)
