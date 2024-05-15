print("Semana No. 10: Ejercicio 2")
mesEntrada = int(input("Ingrese un número del 1-12: "))
mesSalida = ""
match mesEntrada:
    case 1:
        mesSalida = "Enero"
    case 2: 
        mesSalida = "Febrero"
    case 3: 
        mesSalida = "Marzo"
    case 4:
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6:
        mesSalida = "Junio"
    case 7: 
        mesSalida = "Julio"
    case 8: 
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11: 
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    case _: 
        print("Error: El número a ingresar debe estar contenido entre 1")
print(f"Mes: {mesSalida}")

#Actividad 2
print("Semana No. 10: Ejercicio 2")
#Entradas
a = int(input("Ingrese el primer número mayor a cero"))
b = int(input("Ingrese el segundo número mayor a cero"))
c = int(input("Ingrese el tercer número mayor a cero"))

if(a>0 or b <= 0 or c <= 0):
    print("Error: El número debe ser mayor a cero")

#Diagrama
    print("El número(s) mayor es: ")
if (a>b):
    if(a>c):
        print(a)
    else:
        if(a == c):
            print(a,"y",c)
        else:
            print(c)
elif(a == b):
    if(a>c):
        print(a,"y",b)
    elif(a == c):
        print(a,b,c)
elif (b>c):
    print(c)
elif (b == c):
    print(b,c)
else:
    print(c)




