#busqueda binaria
#funcion
def busquedaBinaria(vector,elemento):
    izq=0
    der=len(vector)-1
    while izq<=der:
        med=(izq+der)//2
        #print("izquierda ",izq," -medio ",med," -derecha ",der)
        if elemento==vector[med]:
            return med
        elif vector[med]>elemento:
            der=med-1
        else:
            izq=med+1
    return -1

#programa principal
vector=[1,2,3,4,5,6,7,8,9,10]
print("el vector es: ",vector)
elemento=int(input("elemento a buscar: "))
#llamado funcion
pos=busquedaBinaria(vector,elemento)
if pos==-1:
    print("elemento no encontrado!")
else:
    print("encontrado en la posicion: ",pos)
