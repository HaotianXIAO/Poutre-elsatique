#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

#dimention en mm
h = 150
b = 87
e = 3
I11 = (e * (h**3))/6 + 0.5*e*(b-e)*(h-e)*(h-e)
Omega = (h - e)*(b - e)


# In[2]:


#Foction de transfert de modèle 2D en 3D

def trans(z,x):
    if 0 <= z and z < h-e:
        x1 = 0.5*(b-e)
        x2 = 0.5*(h-e)-z
        x3 = x
        return (x1,x2,x3)
    elif h-e <= z and z < h+b-2*e:
        x1 = h+0.5*b-1.5*e-z
        x2 = -0.5*h+0.5*e
        x3 = x
        return (x1,x2,x3)
    elif h+b-2*e <= z and z < 2*h+b-3*e:
        x1 = -0.5*b+0.5*e
        x2 = -1.5*h-b+2.5*e+z
        x3 = x
        return (x1,x2,x3)
    else:
        x1 = -2*h-1.5*b+3.5*e+z
        x2 = 0.5*h-0.5*e
        x3 = x
        return (x1,x2,x3)


# In[3]:


# Exemple : On essayer de transformer une ligne de modèle 2D en 3D
s = np.arange(0, 300, 1, dtype='float')
t = np.arange(0, 300, 1, dtype='float')
x = np.zeros(300)
y = np.zeros(300)
z = np.zeros(300)
for i in range (0,300):
    x[i] = trans(s[i],t[i])[0]
    y[i] = trans(s[i],t[i])[1]
    z[i] = trans(s[i],t[i])[2]

plt.plot(s,t)


# In[5]:


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


ax.scatter(x, y, z)

ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

plt.show()


# In[ ]:




