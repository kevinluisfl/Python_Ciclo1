
cant=int(input("Cuantos numeros va escribir?: "))
cantp=0
canti=0
sump=0
sumi=0

for i in range(cant):
    num=int(input("Escriba numero: "))
    if num%2==0:
        cantp=cantp+1
        sump=sump+num
        print("El numero ",num," es PAR!")
    else:
        canti=canti+1
        sumi=sumi+num
        print("El numero ",num," es IMPAR!")
    print("nuevo numero...")
print(" ")
print("Cantidad de numeros PARES: ",cantp)
print("Suma de numeros PARES: ",sump)
print(" ")
print("Cantidad de numeros IMPARES: ",canti)
print("Suma de numeros IMPARES: ",sumi)
print("proceso finalizado...")
