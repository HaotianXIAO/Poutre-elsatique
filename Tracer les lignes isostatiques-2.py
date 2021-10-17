#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np
#dimention
l = 10; b = 0.3; h = 1


# In[2]:


#champ des contraintes normales
def sig(x,y):
#    x = x
    y = 6*x*(1-x)*y
    return y
#champ des cpmtraomtes tangentielles
def tau(x,y):
#    x = x
    y = 6*b*(0.5 - x)*(h*h*0.25 - y*y)
    return y


# In[3]:


#les directions principales en fonction de valeur s et t
#regarde page 297
def dir1(s,t):
    s = (0.5*s + math.sqrt(0.25*s*s + t*t) - s)/math.sqrt((0.5*s + math.sqrt(0.25*s*s + t*t) - s)**2+t**2)
    t = -t/math.sqrt((0.5*s + math.sqrt(0.25*s*s + t*t) - s)**2+t**2)
    return s,t

def dir2(s,t):
    s = (0.5*s - math.sqrt(0.25*s*s + t*t) - s)/math.sqrt((0.5*s - math.sqrt(0.25*s*s + t*t) - s)**2+t**2)
    t = -t/math.sqrt((0.5*s - math.sqrt(0.25*s*s + t*t) - s)**2+t**2)
    return s,t


# In[4]:


#les directions principales dans le plan XOY
def du1(x,y):
    y = dir1(sig(x,y),tau(x,y))
    return y

def du2(x,y):
    y = dir2(sig(x,y),tau(x,y))
    return y


# In[5]:


#tracer des lignes isostatiques point par point, p1 et q1 pour lignes de traction et p2 et q2 pour linge de compression
#Nombre de lignes
nlin = 8
#Liste de points initiaux de ces lignes:
def jusiv(j):
    j = h/2 - h/(2*nlin**2) * (j - 1)**2
    return j


# In[14]:


i=1
j=1
x = np.arange(0, 1, 0.01*h, dtype='float')

y = np.arange(0, 1, 0.01*h, dtype='float')

x[0] = 1
y[0] = jusiv(0.2)
for i in range (0,99):
    x[i+1] = x[i] + 0.01*h*du1(x[i],y[i])[0]
    y[i+1] = y[i] + 0.01*h*du1(x[i],y[i])[1]
    
diagrame_v = plt.plot(x,y)


# In[ ]:




