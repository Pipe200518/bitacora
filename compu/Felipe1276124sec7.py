print ("Semana No. 11: Ejercicio 1")

n = int(input("Ingrese un nùmero mayor que 0"))

#declaración de variables
a = 0
b = 1 
c = 0
i = 2 
resultado = ""

if (n>0):
    resultado = str(a)

    if(n>1):
        resultado += ", " + str(b)
        print(resultado)
    while (i<n):
        c = a + b
        resultado += ", " + str(c)
        a = b
        b = c
        i = i + 1
    print ( resultado)
else:
    print(resultado) 

print("Semana No. 11 Ejercicio 2")

n = int(input("Ingrese un nùmero mayor que 0"))

if (n<=0):
    print("Error: el número debe ser mayor que cero")
resultadoA = 0
for x in range (1, n+1):
    resultadoA += (1/x)
print("Inciso A: "+str resultadoA)

print ("Semana No.11: Ejercicio 2 Inciso B")
N= int(input ("INGRESE UN NÚMERO MAYOR A 0: "))

if (N <= 0):
    print("Error! El número debe de ser mayor a 0")

ResultadoB= 0
for y in range (1, N+1):
    ResultadoB += (1/pow(2, y))


print("Inciso B: ", ResultadoB)


print ("Semana No.11: Ejercicio 2 Inciso C")
x= int(input ("INGRESE UN NÚMERO DE X: "))
a= int(input ("INGRESE UN NÚMERO DE a: "))
n= int(input ("INGRESE UN NÚMERO de n: "))

ResultadoC= 0
for k in range (n + 1):
    ResultadoC += (x * k) * (a * (n - k))


print("Inciso C: ", ResultadoC)
