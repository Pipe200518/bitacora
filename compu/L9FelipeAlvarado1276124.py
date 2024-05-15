print("Ejercicio1")

n1=int(input("Ingrese el preimer numero: "))
n2=int(input("Ingrese el segundo numero: "))

divisionReal= n1/n2
iviEntera= n1//n2
divModular= n1%n2
suma = n1+n2
resta = n1-n2
multiplicacion = n1*n2

print(n1,"+",n2,"=",suma)
print(n1,"-",n2,"=",resta)
print(n1,"*",n2,"=",multiplicacion)
print(n1,"/",n2,"=",divisionReal)
print(n1,"//",n2,"=",iviEntera)
print(n1,"%",n2,"=",divModular)

igualdad = n1 == n2
diferentes = n1 != n2
mayor = n1>n2
menor = n1<n2

print(n1,">",n2,"=",mayor)
print(n1,"<",n2,"=",menor)
print(n1,"==",n2,"=",igualdad)
print(n1,"!=",n2,"=",diferentes)

print("ejercicio 3")

a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el segundo numero"))
c = int(input("Ingrese el tercer numero"))

print("i. ",a*b+c)
print("ii. ",a*(b+c))
print("iii. ",a/(b+c))
print("iv. ",(3*a+2*b)/(c**2))

print("Actividad3, Ejercicio 1")
metros1 = int(inpun("Ingrese metros: "))

Km = metros1/1000

print("Km:", Km)

n=int(input("ingrese una cantidad en metros: "))

millas=n/1609
kilometros=n/1000
pies=n*3.28
pulgadas=n*39.37

print("Millas",millas)
print("Kilómetros",kilometros)
print("Pies",pies)
print("Pulgadas",pulgadas)

n2=int(input("Ingrese otra cantidad en metros: "))

yardas=n2*1.094
pies2=n2*3.28
pulgadas2=n2*39.37

print("yardas",yardas)
print("pies",pies2)
print("pulgadas",pulgadas2)