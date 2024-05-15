import random
#Felipe Alvarado 1276124
print("Semana No. 16: Ejercicio 1")


numeros = [random.randint(1, 100) for _ in range(10)]

while True:
    # Mostrar opciones
    print("\nOpciones:")
    print("a. Mostrar los números ingresados.")
    print("b. Mostrar el promedio del arreglo.")
    print("c. Mostrar la longitud del arreglo.")
    print("d. Encontrar y mostrar:")
    print("   i. La suma de posiciones pares")
    print("   ii. La suma de posiciones impares")
    print("e. Salir")

    opcion = input("Ingrese una opción (a, b, c, d, e): ")

    if opcion == 'a':
        print("Números ingresados:", numeros)
    elif opcion == 'b':
        promedio = sum(numeros) / len(numeros)
        print("Promedio del arreglo:", promedio)
    elif opcion == 'c':
        longitud = len(numeros)
        print("Longitud del arreglo:", longitud)
    elif opcion == 'd':
        suma_pares = sum(numeros[::2])  # Sumar números en posiciones pares
        suma_impares = sum(numeros[1::2])  # Sumar números en posiciones impares
        print("Suma de posiciones pares:", suma_pares)
        print("Suma de posiciones impares:", suma_impares)
    elif opcion == 'e':
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")




print("Semana No. 16: Ejercicio 2")


filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))


matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]


numeros_pares = 0
numeros_impares = 0
numero_mayor = float('-inf')
numero_menor = float('inf')


for fila in matriz:
    for numero in fila:
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
        if numero > numero_mayor:
            numero_mayor = numero
        if numero < numero_menor:
            numero_menor = numero


print("\nEstadísticas:")
print("Cant de números pares:", numeros_pares)
print("Cant de números impares:", numeros_impares)
print("Num mayor:", numero_mayor)
print("Num menor:", numero_menor)
