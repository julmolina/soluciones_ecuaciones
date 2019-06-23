import statistics
from math import sqrt
#Coeficientes de la ecuación de tercer grado
a3=float(input("Ingresar coeficiente de grado 3 = \n"))
a2=float(input("Ingresar coeficiente de grado 2= \n"))
a1=float(input("Ingresar coeficiente de grado 1= \n"))
a0=float(input("Ingresar término independiente= \n"))
'''
a3=1
#a3=1
a2=-3
#a2=-4
a1=-4
#a1=-3
a0=12
#a0=-10
'''
a0mod=abs(a0)
a3mod=abs(a3)
#Algoritmo para los divisores del término independiente
print ("Absoluto de término independiente =",a0mod)
i=1
p=[]
pn=[]
while (a0mod >=i):
    div=a0mod%(i)
    if (div==0):
        p.append(i)
    i=i+1
for i in range (len(p)):
    pn.append(p[i]*-1)
print ("Los números divisibles de este témino independiente serán = ")
print ('p =',p)
print ('pn =',pn)
#Algoritmo para los divisores del coeficiente principal
print ("Absoluto del coeficiente principal de orden 3 =",a3mod)
i=1
q=[]
qn=[]
while (a3mod >=i):
    div=a3mod%(i)
    if (div==0):
        q.append(i)
    i=i+1
for i in range (len(q)):
    qn.append(q[i]*-1)
print ("Los números divisibles de este coeficiente principal de orden 3 = ")
print ('q =',q)
print ('qn =',qn)
#Algoritmo para las posibles raices racionales
i=1
i2=1
pqr1=[]
pqrn1=[]
for i in range (len(p)):
    for i2 in range (len(q)):
        pqr1.append(p[i]/q[i2])
for i in range (len(p)):
    for i2 in range (len(qn)):
        pqrn1.append(p[i]/qn[i2])
print ("Las posibles raices racionales son ")
print ('p/q 1=',pqr1)
print ('p/q n1 =',pqrn1)
#Algoritmo para la división sintetica
pol=[a3,a2,a1,a0]
poldiv=[]
poldiv2=[]
print('El orden del polinomio =',pol)

#Prueba con ciclo while
i=0
while (i<(len(pqr1) or len(pqrn1))):
    poldiv.append(pol[0])
    poldiv2.append(pol[0])
    p1=pol[0]*pqr1[i]+pol[1]
    p11=pol[0]*pqrn1[i]+pol[1]
    poldiv.append(p1)
    poldiv2.append(p11)
    p2=p1*pqr1[i]+pol[2]
    p22=p11*pqrn1[i]+pol[2]
    poldiv.append(p2)
    poldiv2.append(p22)
    p3=p2*pqr1[i]+pol[3]
    p33=p22*pqrn1[i]+pol[3]
    poldiv.append(p3)
    poldiv2.append(p33)
    if (p3==0):
        solrac=pqr1[i]
        a=pol[0]
        b=p1
        c=p2
        disc=((b*b)-4*a*c)
        imag='j'
        if(a!=0):
            if(disc<0):
                disc2=disc*-1
                x12=(-b)/(2*a)
                x1imag=+(sqrt(disc2))/(2*a)
                x2imag=-(sqrt(disc2))/(2*a)
                print("Las tres raices de la ecuación son =")
                print("X = (",x12,")+( ",x2imag,")",imag)
                print("X = (",x12,")+( ",x1imag,")",imag)
                
            else:
                x1=(-b+(sqrt(disc)))/(2*a)
                x2=(-b-(sqrt(disc)))/(2*a)
                print("Las tres raices de la ecuación son:")
                print("X = ",x2)
                print("X = ",x1)
                
        break;
    if (p33==0):
        solrac=pqrn1[i]
        a=pol[0]
        b=p11
        c=p22
        disc=((b*b)-4*a*c)
        imag='j'
        if(a!=0):
            if(disc<0):
                disc2=disc*-1
                x12=(-b)/(2*a)
                x1imag=+(sqrt(disc2))/(2*a)
                x2imag=-(sqrt(disc2))/(2*a)
                print("Las tres raices de la ecuación son =")
                print("X = (",x12,")+( ",x2imag,")",imag)
                print("X = (",x12,")+( ",x1imag,")",imag)
                
            else:
                x1=(-b+(sqrt(disc)))/(2*a)
                x2=(-b-(sqrt(disc)))/(2*a)
                print("Las tres raices de la ecuación son:")
                print("X = ",x2)
                print("X = ",x1)
        break;
    i=i+1

#print('pol_división =',poldiv)
#print('pol_división_neg =',poldiv2)
print('X =',solrac)

'''
Validación:
https://www.youtube.com/watch?v=UXBVQJnIQMQ
https://www.youtube.com/watch?v=j5AfFpeUBEs
https://www.youtube.com/watch?v=VYm88rbo4KA
'''
