print("Semana No. 12: Ejercicio 1 ")

print("a. Sumatoria", "b. Factorial", "c. Tablas de multiplicar", "d. Número perfecto", sep = "\n")
opcion = input("Ingrese la letra de su opción: ")
match opcion:
    case "a":
        n = int(input("Ingrese un número entero positivo "))
        if (n > 0):
            sumatoria = 0
            i = 1
            while(i<= n):
                sumatoria = sumatoria + 1
                i = i + 1
                print("Sumatoria es: ", sumatoria)
        else: 
            print("Error, el número debe ser mayor a 0 ")
    
    case "b":
        n =0
        while n <= 0:
            n = int(input("Ingrese un número entero positivo: "))
            if n >= 0:
                print ("Error, el número debe ser entero positivo ")
                factorial = 1
                for x in range(1, n + 1):
                    factorial*= x
                    print("la factial es: ", factorial)
     
    

    case "c":
        tcoulumnas = "\t"
        for i in range(1, 11):
            tcoulumnas = tcoulumnas + str(i) + "\t"
        print(tcoulumnas)

        for filas in range(1, 11):
            columnasfila = str(filas) + "\t"
            for columnas in range(1, 11):
                columnasfila = columnasfila + str(filas * columnas) + "\t"
              
            print(columnasfila)

    case "d":
        ent=int(input("Ingrese un número entero: "))
for i in range(2, ent+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto" %i)