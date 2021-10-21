import matplotlib.pyplot as plt
import numpy as np


l = 0.9
b = 0.087
h = 0.15
e = 0.003
omega = (b-e)*(h-e)

eps = 0.01 #longueur de pas
t = 164.4
P = 400
R = 600

I = b*h**3/12-(b-2*e)*(h-2*e)**3/12  # Moment d'inertie

### Seeds poour le tracé des lignes isostatiques

nlin = 4 # nombre de lignes

#seed pour tracer les courbes
seeds1 = np.array([[(l/3)*i/nlin,0] for i in range(nlin+1)])
seeds2 = np.array([[(l/3)*i/nlin,0] for i in range(nlin+1)]+[[l/6,-h*(i-nlin/2)/(nlin*2)] for i in range(nlin+1)])

#face et section: voir figure 8.34 et 8.35 pour dans le page 294 et 295

gauche = 1
bas = 2
droite = 3
haut = 4

#Géométie de poutre dans le plan (x,s)

##################################################################
# (bas,section1)    #  (bas,section2)     #  (bas,section3)      #
#                   #                     #                      #
# (gauche,section1) #  (gauche,section2)  #  (gauche,section3)   #
#                   #                     #                      #
# (haut,section1)   #  (haut,section2)    #  (haut,section3)     #
#                   #                     #                      #
# (droite,section1) #  (droite,section2)  #  (droite,section3)   #
##################################################################

#M,V,T dans le plans (x,s) pour différent section
def M(x,section):
    if section==1:
        return P*x
    if section==2:
        return (-P/2)*(x-(l/3))+(P*l)/2 
    if section==3:
        return ((-3)*P*(x-((2*l)/3)))/2+(P*l)/3 

def V(x,section):
    if section==1:
        return P
    if section==2:
        return P-R
    if section==3:
        return -R

def T(x,section):
    if section==1:
        return 0
    else:
        return t


#sigma et tau dans le plans (x,s) pour différent section et face

def sig(x,s,section,face):
    if face==gauche or face==droite:
        return -M(x,section)*s/I
    if face==haut:
        return -M(x,section)*h/(2*I)
    if face==bas:
        return M(x,section)*h/(2*I)

#tau ne dépend pas de T

def tau(x,s,section,face):
    if face==gauche:
#        return V(x1,section)/(I*e)*((h/2-x2)*e*(h/2-(h/2-x2)/2) + b/2*e*(h/2-e)) - T(x1,section)/(2*e*omega)
        return V(x,section)/(I*e)*((h/2-s)*e*(h/2-(h/2-s)/2) + b/2*e*(h/2-e))
    if face==droite:
        return V(x,section)/(I*e)*((h/2-s)*e*(h/2-(h/2-s)/2) + b/2*e*(h/2-e))
#        return V(x1,section)/(I*e)*((h/2-x2)*e*(h/2-(h/2-x2)/2) + b/2*e*(h/2-e)) + T(x1,section)/(2*e*omega)
    if face==haut:
#        return V(x1,section)*x2/(I)*(h/2-e/2) - T(x1,section)/(2*e*omega)
        return V(x,section)*s/(I)*(h/2-e/2)
    if face==bas:
#       return V(x1,section)*x2/(I)*(h/2-e/2) + T(x1,section)/(2*e*omega)
        return V(x,section)*s/(I)*(h/2-e/2) + T(x,section)/(2*e*omega)

#page 297 page 327
#s=sigma t=tau
def dir1(s,t): 
    n1 = s/2 + (s**2/4 + t**2)**0.5 - s
    n2 = -t
    norm = (t/abs(t))*(n1**2+n2**2)**0.5
    if abs(t)>0.001:
        return np.array([n1,n2]/norm)
    elif s>0:
        return np.array([0,-1])
    else:
        return np.array([-1,0])


def dir2(s,t): 
    n1 = s/2 - (s**2/4 + t**2)**0.5 - s
    n2 = -t
    norm = (t/abs(t))*(n1**2+n2**2)**0.5
    if abs(t)>0.001:
        return np.array([n1,n2]/norm)
    else:
        return np.array([0,1])



def Isostat(section,face,seeds):

    plt.figure()
    boxX = np.array([0,l/3,l/3,0,0])
    boxY = np.array([-h/2,-h/2,h/2,h/2,-h/2])
    
    ### Definition de la zone de la poutre
    if face==bas or face==haut:
        boxY *= b/h
        def testA(pos):
            return (pos[0] >= 0 and pos[0] <= l/3 and pos[1] >= -b/2 and pos[1] <= b/2)
    else:
        def testA(pos):
            return (pos[0] >= 0 and pos[0] <= l/3 and pos[1] >= -h/2 and pos[1] <= h/2)

    plt.plot(boxX,boxY,'black')
    plt.axis('equal')
#changement de variable
    def du1(x,s):
        return dir1(sig(x,s,section,face),tau(x,s,section,face))

    def du2(x,s):
        return dir2(sig(x,s,section,face),tau(x,s,section,face))

    for s in seeds:
        p2 = np.array([s])
        i = 0
        while testA(p2[i]):
            p2 = np.append(p2,[p2[-1]+eps*h*du2(p2[i][0],p2[i][1])],axis=0)
            i = i+1
        plt.plot(p2[:,0],p2[:,1],'r',linewidth=2)
        
        p1 = np.array([s])
        i = 0
        while testA(p1[i]):
            p1 = np.append(p1,[p1[-1]-eps*h*du1(p1[i][0],p1[i][1])],axis=0)
            i = i+1
        plt.plot(p1[:,0],p1[:,1],'b',linewidth=2)

        q2 = np.array([s])
        i = 0
        while testA(q2[i]):
            q2 = np.append(q2,[q2[-1]-eps*h*du2(q2[i][0],q2[i][1])],axis=0)
            i = i+1
        plt.plot(q2[:,0],q2[:,1],'r',linewidth=2)

        q1 = np.array([s])
        i = 0
        while testA(q1[i]):
            q1 = np.append(q1,[q1[-1]+eps*h*du1(q1[i][0],q1[i][1])],axis=0)
            i = i+1
        plt.plot(q1[:,0],q1[:,1],'b',linewidth=2)
    plt.show()

Isostat(1,gauche,seeds1)
Isostat(2,gauche,seeds1)
Isostat(3,gauche,seeds1)

Isostat(1,bas,seeds2)
Isostat(2,bas,seeds1)
Isostat(3,bas,seeds1)

Isostat(1,haut,seeds2)
Isostat(2,haut,seeds1)
Isostat(3,haut,seeds1)

Isostat(1,droite,seeds1)
Isostat(2,droite,seeds1)
Isostat(3,droite,seeds1)


#######################################################################################
# Trace en 3d
#######################################################################################

fig = plt.figure()
ax = fig.gca(projection='3d')

def Isostat3d(section,face,seeds):
    boxX = np.array([0,l/3,l/3,0,0])
    boxY = np.array([-b/2,-b/2,b/2,b/2,-b/2])
    boxZ = np.array([0]*5)

    ### Valeurs pour le placement de la surface dans l'espace 3d
    L_offset = (section-1)*l/3 #Offset dans le sens de la longeur de la poutre
    H_offset = 0. #Offset horizontal
    V_offset = 0. #Offset vertical
    vertical = True
    if face == gauche or face == droite:
        vertical = True
        if face == droite:
            H_offset = b/2
            V_offset = 0
        else:
            H_offset = -b/2
            V_offset = 0
    else:
        vertical = False
        if face == haut:
            H_offset = 0
            V_offset = h/2
        else:
            H_offset = 0
            V_offset = -h/2


    if vertical:
        boxY *= (h/b)
        boxY,boxZ = boxZ,boxY
        def testA(pos):
            return (pos[0] >= 0 and pos[0] <= l/3 and pos[1] >= -h/2 and pos[1] <= h/2)
    else:
         def testA(pos):
            return (pos[0] >= 0 and pos[0] <= l/3 and pos[1] >= -b/2 and pos[1] <= b/2)

    ax.plot(boxX+L_offset,boxY+H_offset,boxZ+V_offset,'black')

    def du1(x1,x2):
        return dir1(sig(x1,x2,section,face),tau(x1,x2,section,face))
    def du2(x1,x2):
        return dir2(sig(x1,x2,section,face),tau(x1,x2,section,face))

    X = np.array([])
    Y = np.array([])
    Z = np.array([])

    for s in seeds:
        p2 = np.array([s])
        i = 0
        while testA(p2[i]):
            p2 = np.append(p2,[p2[-1]+eps*h*du2(p2[i][0],p2[i][1])],axis=0)
            i = i+1
        X = np.array(p2[:,0])
        Y = np.array(p2[:,1])
        Z = np.array([0]*len(X))
        if vertical:
            Y,Z = Z,Y
        ax.plot(X+L_offset,Y+H_offset,Z+V_offset,'r',linewidth=1)

        p2 = np.array([s])
        i = 0
        while testA(p2[i]):
            p2 = np.append(p2,[p2[-1]-eps*h*du1(p2[i][0],p2[i][1])],axis=0)
            i = i+1
        X = np.array(p2[:,0])
        Y = np.array(p2[:,1])
        Z = np.array([0]*len(X))
        if vertical:
            Y,Z = Z,Y
        ax.plot(X+L_offset,Y+H_offset,Z+V_offset,'b',linewidth=1)

        p2 = np.array([s])
        i = 0
        while testA(p2[i]):
            p2 = np.append(p2,[p2[-1]-eps*h*du2(p2[i][0],p2[i][1])],axis=0)
            i = i+1
        X = np.array(p2[:,0])
        Y = np.array(p2[:,1])
        Z = np.array([0]*len(X))
        if vertical:
            Y,Z = Z,Y
        ax.plot(X+L_offset,Y+H_offset,Z+V_offset,'r',linewidth=1)

        p2 = np.array([s])
        i = 0
        while testA(p2[i]):
            p2 = np.append(p2,[p2[-1]+eps*h*du1(p2[i][0],p2[i][1])],axis=0)
            i = i+1
        X = np.array(p2[:,0])
        Y = np.array(p2[:,1])
        Z = np.array([0]*len(X))
        if vertical:
            Y,Z = Z,Y
        ax.plot(X+L_offset,Y+H_offset,Z+V_offset,'b',linewidth=1        )


Isostat3d(1,gauche,seeds1)
Isostat3d(1,bas,seeds2)
Isostat3d(1,droite,seeds1)
Isostat3d(1,haut,seeds2)

Isostat3d(2,gauche,seeds1)
Isostat3d(2,bas,seeds1)
Isostat3d(2,droite,seeds1)
Isostat3d(2,haut,seeds1)

Isostat3d(3,gauche,seeds1)
Isostat3d(3,bas,seeds1)
Isostat3d(3,droite,seeds1)
Isostat3d(3,haut,seeds1)


ax.set_xlim(0,l)
ax.set_ylim(-l/2, l/2)
ax.set_zlim(-l/2, l/2)
plt.show()