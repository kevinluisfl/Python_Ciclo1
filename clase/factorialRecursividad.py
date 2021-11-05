# Programa para calcular el factorial CON recursividad
# Autor: Sergio Medina
# Fecha: 16/06/2021

#Funciones
def factorial(numero):
    if numero==0 or numero==1:
        return 1
    else:
        return numero*factorial(numero-1)
#Programa principal
numero=int(input("Ingrese número: "))
#LLamado a la función
fact=factorial(numero)
print("Factorial: ",fact)


# numero=4
# factorial(4)=4*factorial(3)
# factorial(4)=4*3*factorial(2)
# factorial(4)=4*3*2*factorial(1)
# factorial(4)=4*3*2*1
