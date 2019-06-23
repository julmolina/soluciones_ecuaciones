#Funciones para la soluciones de ecuaciones de 1er. grado de una, dos y tres incognitas
def ecua1():
    #Solución de ecuación de una incognita
    print('Solución de ecuación de una incognita')
    x1=float(input('Ingresar el coeficiente de X ='))
    x0=float(input('Ingresar el término independiente ='))
    x=((-x0)/x1)
    print ('El resultado de la variable es :')
    print ('X = ',x)

def ecua2():
    #Solución de ecuaciones simultaneas de dos incognitas
    print('Solución de ecuaciones simultaneas de dos incognitas')
    print('De la Primera Ecuación')
    x1=float(input('Ingresar el coeficiente de X ='))
    y1=float(input('Ingresar el coeficiente de Y ='))
    y0=float(input('Ingresar el término independiente ='))
    print('De la Segunda Ecuación')
    x11=float(input('Ingresar el coeficiente de X ='))
    y11=float(input('Ingresar el coeficiente de Y ='))
    y01=float(input('Ingresar el término independiente ='))
    y=((-y0*x11)+(y01*x1))/((y1*x11)-(y11*x1))
    x=((-y0)-(y1*y))/(x1)
    print ('El resultado de las variables es :')
    print ('X = ',x)
    print ('Y = ',y)

def ecua3():
    #Solución de ecuaciones simultaneas de tres incognitas
    print('Solución de ecuaciones simultaneas de tres incognitas')
    print('De la Primera Ecuación')
    x0=float(input('Ingresar el coeficiente de X ='))
    y0=float(input('Ingresar el coeficiente de Y ='))
    z0=float(input('Ingresar el coeficiente de Z ='))
    a0=float(input('Ingresar el término independiente ='))
    print('De la Segunda Ecuación')
    x1=float(input('Ingresar el coeficiente de X ='))
    y1=float(input('Ingresar el coeficiente de Y ='))
    z1=float(input('Ingresar el coeficiente de Z ='))
    a1=float(input('Ingresar el término independiente ='))
    print('De la Tercera Ecuación')
    x2=float(input('Ingresar el coeficiente de X ='))
    y2=float(input('Ingresar el coeficiente de Y ='))
    z2=float(input('Ingresar el coeficiente de Z ='))
    a2=float(input('Ingresar el término independiente ='))
    z=(((-a0*x1)*((y0*x2)-(y2*x0)))+((a1*x0)*((y0*x2)-(y2*x0)))+((a0*x2)*((y0*x1)-(y1*x0)))-((a2*x0)*((y0*x1)-(y1*x0))))/((((z0*x1)-(z1*x0))*((y0*x2)-(y2*x0)))-(((z0*x2)-(z2*x0))*((y0*x1)-(y1*x0))))
    y=(((-a0*x2)+(a2*x0))-(((z0*x2)-(z2*x0))*z))/((y0*x2)-(y2*x0))
    x=(-a0-(y0*y)-(z0*z))/x0
    print ('El resultado de las variables es :')
    print ('X = ',x)
    print ('Y = ',y)
    print ('Z = ',z)

#Programa principal
print ('Del siguiente menú, que tipo de ecuación escogera:')
print ('1. Ecuación de una incognita')
print ('2. Ecuación de dos incognitas')
print ('3. Ecuación de tres incognitas')
m=int(input('Seleccione el número :'))
if (m==1):
    ecua1()
if (m==2):
    ecua2()
if (m==3):
    ecua3()
if (m!=1 and m!=2 and m!=3) :
    print ("No es la opción correcta !")
'''
Validación
https://www.youtube.com/watch?v=lLPcHVAqY80
'''
