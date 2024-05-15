print("Felipe Alvarado ")
numeros=[]
n=int(input("Ingrese un valor: "))
numeros.append(n)
while(n>-1):
    n=int(input("Ingrese un valor: "))
    numeros.append(n) 

print("Arreglo:",numeros)
numeros.reverse()
print("Arreglo del inverso:",numeros) 
print("")
mayor=numeros[0]
for i in range(numeros[0],numeros[-1]):
    if numeros[i]>mayor:
        mayor=numeros[i]
print("Número superior en el arreglo:",mayor) 
for i in range(numeros[0],numeros[-1]):
    if numeros[i]<mayor:
        mayor=numeros[i]
print("Número inferior en el arreglo:",mayor)