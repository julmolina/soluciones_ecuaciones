import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
a=float(input("Ingresar coeficiente cuadratico = \n"))
b=float(input("Ingresar coeficiente lineal= \n"))
c=float(input("Ingresar término independiente= \n"))
print("LA ECUACIÓN DE 2DO. GRADO : ")
print("F(X)=(",a,")X^2+(",b,")X","+(",c,")")
disc=((b*b)-4*a*c)
imag='j'
if(a!=0):
    if(disc<0):
        disc2=disc*-1
        x12=(-b)/(2*a)
        x1imag=+(sqrt(disc2))/(2*a)
        x2imag=-(sqrt(disc2))/(2*a)
        print("Las raices de la ecuación :")
        print("X1 = (",x12,")+( ",x1imag,")",imag)
        print("X2 = (",x12,")+( ",x2imag,")",imag)
    else:
        x1=(-b+(sqrt(disc)))/(2*a)
        x2=(-b-(sqrt(disc)))/(2*a)
        print("Las raices de la ecuación :")
        print("X1 = ",x1)
        print("X2 = ",x2)
else:
    print("El coefiente cuadratico debe ser diferente de cero")

