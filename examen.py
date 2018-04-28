print ("Menu:")
print ("0.Comparacion de numeros.\n1. Suma\n2. Resta.\n3. Division.")
print ("4.IVA \n5. Multiplicacion dos digitos.")
print("6.Multiplicacionde de clase")
print ("7. Salir")

def comparacion ():
    a=int (input("Dame el numero a "))
    b=int (input("Dame el numero b "))
    c=int (input("Dame el numero c "))
    if a==b==c:
        print(a," los numeros son iguales ",b," y ",c)
    if a<b:
        print (a," es menor que",b)
    elif a>b:
        print (a,"es mayor que",b)
    if a>c:
        print (a,"es mayor que",c)
    elif a<c:
        print (a," es menor que",c)
    if a==c:
        print (a," es igual a ",c)
    elif a==b:
        print (a," es igual a ",b)

def suma():
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La suma de los dos numeros es",a+b)
def resta ():
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La resta de los dos numeros",a,"menos",b," es:",a-b)
def division ():
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La division de los dos numeros es ",a/b)
def iva():
    iva=float (input("1.Ingrese el IVA:"))
    cantidad= float (input("2.Ingrese la cantidad:"))
    print ("La cantidad es:",cantidad)
    print ("El iva es:",iva*cantidad)
def multiplicacion ():
    a=int (input("Ingresa un numero"))
    b=int (input("Ingresa otro numero"))
    print ("La multiplicacion de los dos numeros es",a*b)
def multiplicacion_indel ():
    print("Multiplicacion de la tabla")
    m=int (input ("Elige la tabla de multiplicar que desees "))
    o=int (input ("El valor final del rango "))
    for u in range(1,o+1):
        print (u,"*",m,"=",u*m)
n=int (input("Dame la opcion:"))
while 6>=n:
    while 0<=n:
        if n==0:
            comparacion ()
        if n==1:
            suma ()
        if n==2:
            resta ()
        if n==3:
            division ()
        if n==4:
            iva ()
        if n==5:
            multiplicacion ()
        if n==6:
            multiplicacion_indel ()
        n=-1
    n=int (input("Elige otra opcion"))
print ("Esta fuera del ciclo")


