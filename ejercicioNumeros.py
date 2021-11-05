#Numeros entre dos numeros dados

from sys import exit

num1= int(input("Escriba el primer numero: "))
num2= int(input("Escriba el segundo numero: "))
men=0
may=0

if num1 < num2:
    men=num1
    may=num2
elif num2 < num1:
    men=num2
    may=num1
else:
    print("Los dos numeros son iguales...")
    exit("Bye!")

print("Los numeros entre ",men," y ",may," son: ")

men+=1
if men == may:
    print("No hay enteros entre ",men-1," y ",may)
    exit("Bye!")
    
while men < may:
    print(men)
    men+=1


#El RETURN solo funciona dentro de FUNCINOES, el BREAK dentro de CICLOS
#para estos condicionales toca usar EXIT() o QUIT()
