## Dimension de la poutre a definir#
l=int(input("saisir la longeur l de la poutre, l="))
b=int(input("saisir la largeur b de la poutre, b="))
h=int(input("saisir la hauteur h de la poutre, h="))
e=int(input("saisir l'epaisseur e de la poutre, e="))
##Definir constante du probleme##
I=((((1/12)*(e**3)*b)+0.25*((h-e)**2))*2)+((1/6)*e*(h-2*e)**3)
A=(2*h+2*b)*e
## Moment statique ##
def MS(x,s):
    x1=trans(x,s)[1]
    x2=trans(x,s)[2]
    if (s<h-e or (s<2*h+b-3*e and s>=h+b-2*e)):
        n=(b*e*0.5)*(h-e)+e*((0.5*h-e)**2-abs(x2)**2)
    else:
        n=0.5*(h*e)*(b-e)+0.5*e*(0.25*b**2-abs(x1)**2)
    return n
## Contraintes to sigma ##
def sigma(x,s):
    sigma=M(x)*x2/I
    return sigma
def to(x,s):
    x1=trans(x,s)[1]
    x2=trans(x,s)[2]
    if s<h-e or (s<2*h+b-3*e and s>=h+b-2*e):
        a=h-2*e
    else:
        a=e
    to=V(x)*MS(x,s)/(a*I)
    return to

