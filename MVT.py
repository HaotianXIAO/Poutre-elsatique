#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.axes as As 
from math import *

# Constants
l=900           #mm
b=75            #mm
h=150           #mm
e=3             #mm
O=(b-e)*(h-e)   #mm2
I=(b*h**3-(b-2*e)*(h-2*e)**3)/12    #mm4
P=100           #N
ftu=fcu=10 #MPa
E=10000 #Mpa


# In[ ]:


def M(x3):
    if 0 <=x3<(l/3):
        return P*x3
    elif (l/3)< x3 <((2*l)/3):
        return ((-P/2)*(x3-(l/3)))+((P*l)/2) elif ((2*l)/3)< x3 <=l :
    return (((-3)*P*(x3-((2*l)/3)))/2)+((P*l)/3) else :
        return 0


def T(x3):
    if 0 <=x3<(l/3):
        return 0
    elif (l/3)< x3 <=((2*l)/3):
        return ((1/0.364)*P*l)/6 
    elif ((2*l)/3)<= x3 <=l :
        return ((1/0.364)*P*l)/6 
    else:
        return 0
    
def V(x3):
    if 0 <=x3<(l/3):
        return P
    elif (l/3)< x3 <=((2*l)/3):
        return -P/2
    elif ((2*l)/3)<= x3 <=l:
        return-3*P/2 
    else:
        return 0




