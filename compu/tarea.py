#Felipe Alvarado 1276124
print("Felipe A. 1276124")

n = 0

while n != 5:
    print('Elija la opción a calcular:')
    print('1) Número perfecto')
    print('2) Proyección de pago')
    print('3) Número primo')
    print('4) Sumatoria por una semana')
    print('5) Salir')
    
    n = int(input())
    print()

    if n == 1:
        N = 0
        print("NÚMERO PERFECTO")
        while N <= 0:
            N = int(input('Ingrese un número entero positivo: '))
            if N <= 0:
                print('El número ingresado debe ser entero positivo') 

        acumulador = 0
        for i in range(1, N):
            if N % i == 0:
                acumulador += i

        if N == acumulador:
            print('Es perfecto')
        else:
            print('No es perfecto')
        print()

    elif n == 2:
        print("PROYECCIÓN DE PAGOS")
        sumatoria = 0
        for i in range(1, 13):
            print("Mes", i, "\t", end="")
        print()
        for j in range(1, 13):
            J = 10 * j
            print("Q", J, "\t", end="")
            sumatoria += J
        print()
        print()
        print()
        print("Total pagado después de 12 meses: Q", sumatoria)
        print()

    elif n == 3:
        N = int(input("Número primo\nIngrese un valor: "))
        if N > 1:
            for i in range(2, N):
                if (N % i) == 0:
                    print("No es primo")
                    break
            else:
                print("Es primo")
        else:
            print("No es primo")
        print()

    elif n == 4:
        print("DINERO AHORRADO ENTRE SEMANA")
        acumulador = 0
        for i in range(7):
            print("Día", i + 1)
            N = int(input("Q"))
            acumulador += N
            print("Total Acumulado: Q", acumulador)
            print()
        print("Total final es: Q", acumulador)
        print()

    elif n == 5:
        print("Gracias")
    else:
        print("Valor no es una opción")
        print()
            