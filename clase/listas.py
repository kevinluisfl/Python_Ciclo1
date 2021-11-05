
#capturar cantidad de datos a ingresar en la lista
print("...inicializar proceso")
n=int(input("ingrese la cantidad de datos de la lista: "))

#inicializar lista vacia
numeros=[]

#llenar lista
for i in range(n):
    num=int(input(f"ingrese dato #{i+1} de {n}: "))
    numeros.append(num)

print(" ")
print("Los datos ingresados fueron: ",numeros)
print(" ")

#inicializar contadores
cpo=0
cne=0
cce=0

#clasificar datos
for i in range(len(numeros)):
    if numeros[i] > 0:
        print("positivo ", numeros[i])
        cpo+=1
    elif numeros[i] < 0:
        print("negativo ", numeros[i])
        cne+=1
    else:
        print("cero ", numeros[i])
        cce+=1

#imprimir resultados
print(" ")
print("Cantidad de positivos: ", cpo)
print("Cantidad de negativos: ", cne)
print("Cantidad de ceros: ", cce)
print("fin proceso...")
