#Felipe Alvarado 1276124
#Ejercicio 1
print("Semana No. 12: Ejercicio 1")
print("")
import math

def AreaTriangulo(base,altura):
    A=(base*altura)/2
    print(f"El área es de {A}")

def AreaCuadrado(lado):
    A=(lado)**2
    print(f"El área es de {A}")

def AreaReactagulo(base,altura):
    A=(base*altura)
    print(f"El área es de {A}")

def AreaCirculo(radio):
    A=(math.pi)*(radio)**2
    print("El área es de",A)

print("Menú")
print("a. Área de triángulo","b. Área de cuadrado ", "c. Área de rectángulo ", "d. Área de círculo", sep="\n")
print("")
opcion=input("Ingrese su opción: ")
print("")
match opcion:
    case "a":
        print("Área de un triángulo")
        base=int(input("Ingrese la base del triángulo: "))
        altura=float(input("Ingrese la altura del triángulo: "))
        AreaTriangulo(base,altura)
    case "b":
        print("Área de un cuadrado")
        lado=float(input("Ingrese el lado del cuadrado: "))
        AreaCuadrado(lado)
    case "c":
        print("Área de un reactángulo")
        base=float(input("Ingrese la base del rectángulo: "))
        altura=float(input("Ingrese la altura del rectángulo: "))
        AreaReactagulo(base,altura)
    case "d":
        print("Área de un círculo")
        radio=float(input("Ingrese el radio del círculo: "))
        AreaCirculo(radio)
print("")

#Ejercicio 2
print("Semana No. 12: Ejercicio 2")
print("")

x = 0 
y = 0

def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

print(f"Posición actual: [{x}][{y}]")
while True:
    print("Menú")
    print("a. Sube","b. Baja ", "c. Izquierda ", "d. Derecha","e. Salir", sep="\n")
    opcion=input("Ingrese su opción: ")
    print("")
    match opcion:
        case "a":
            MoverPosicion(0,1)
        case "b":
            MoverPosicion(0,-1)
        case "c":
            MoverPosicion(-1,0)
        case "d":
            MoverPosicion(1,0) 
        case "e":
            print(f"Coordenadas finales del personaje: [{x}][{y}]")
            break
        case _:
            print("Error: Ingrese una opción dentro del rango")
    print(f"Posición actual: [{x}][{y}]")