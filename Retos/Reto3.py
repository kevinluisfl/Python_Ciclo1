#Reto 3: Operaciones con conjuntos
#Autor: Kevin Luis Flórez Lozada
#Fecha: 05/06/2021

print("Inicio proceso operaciones con conjuntos...")
print("")
#Conjunto A
A=set()
while True:
    try:
        N=int(input("Ingrese la cantidad de elementos para el conjunto A: "))
        if N<1:
            print("Error! La cantidad debe ser mayor a 0. Intenta de nuevo...")
            continue
        break
    except ValueError:
            print("Error! Debe ser entero Intenta de nuevo...")
for i in range(N):
    A.add(input(f"Ingrese el elemento {i+1} de {N} del conjunto A: "))
#
print("")
#Conjunto B
B=set()
while True:
    try:
        M=int(input("Ingrese la cantidad de elementos para el conjunto B: "))
        if M<1:
            print("Error! La cantidad debe ser mayor a 0. Intenta de nuevo...")
            continue
        break
    except ValueError:
            print("Error! Debe ser entero Intenta de nuevo...")

for i in range(M):
    B.add(input(f"Ingrese el elemento {i+1} de {M} del conjunto B: "))
#
print("")
#Impresión de resultados
print("El Conjunto A es: ", A)
print("El Conjunto B es: ", B)

print("")
#Operación INTERSECCIÓN
print("-La Operación INTERSECCIÓN")
#C = A & B
C = A.intersection(B)
print("Conjunto C: ", C)
print("")

#Operación UNIÓN
print("-La Operación UNIÓN")
#D = A | B
D = A.union(B)
print("Conjunto D: ", D)
print("")

#Operación DIFERENCIA
print("-La Operación DIFERENCIA")
#E = A - B
E = A.difference(B)
print("Conjunto E: ", E)
print("")

#Operación DIFERENCIA SIMÉTRICA
print("-La Operación DIFERENCIA SIMÉTRICA")
#F= A ^ B
F= A.symmetric_difference(B)
print("Conjunto F: ", F)
print("")
print("...Fin proceso operaciones con conjuntos")
