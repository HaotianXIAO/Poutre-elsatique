#1e_Question
h=150 #mm
b=87 #mm
e=3 #mm
l=2000 #mm
x1=float(input('x1= '))
if   (x1>(b/2) or x1<(-b/2)):
    print('The valeur is incorrect')
    x1=float(input('x1= '))
x2=float(input('x2= '))
if   (x2>(h/2) or x2<(-h/2)):
    print('The valeur is incorrect')
    x2=float(input('x2='))
x3=float(input('x3= '))
if   (x3>l or x3<0):
    print('The valeur is incorrect')
    x3 = float(input('x3= '))
x=x3
def facette(n,m,p):
    s = 0
    if n==b/2 and (-h/2)<=m<=(h/2) :
        s=h/2-e-m
    elif m==(-h/2) and (-b/2)<=n<=(b/2):
            s = h - 2*e + b / 2 - n
    elif n==-b/2 and (-h/2)<=m<=(h/2) :
            s= h + b - 2*e + (h/2 - e + m)
    elif m==(h/2) and (-b/2)<=n<=(b/2):
            s= 2*h + b - 3*e + (b/2 - e + m)
    return (x,s)
if ((-h / 2)+e) < x1 < ((h / 2)-e) and ((-h / 2)+e) < x2 < ((h / 2)-e):
    print("!Le point choisi n'est pas sur la surface" )
else:
    print('Les coordonnees en 2D (x,s)=',facette(x1,x2,x3))





