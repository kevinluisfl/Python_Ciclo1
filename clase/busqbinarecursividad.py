#Porgrama para la búsqueda binaria recursiva
#Autor: Sergio Medina
#Fecha: 11/06/2021

#Funciones
def busqueda_binaria(vector,info_buscar,izq,der):
    if izq>der:
        return -1
    else:
        med=(izq+der)//2
        if info_buscar==vector[med]:
            return med
        elif info_buscar<vector[med]:
            return busqueda_binaria(vector,info_buscar,izq,med-1)
        else:
            return busqueda_binaria(vector,info_buscar,med+1,der)

#Programa principal
vector=[1,2,3,4,5,6,7,8,9,10]
print ("Lista: ",vector)
info_buscar=int(input("Información a buscar: "))
#Llamado a la función
izq=0
der=len(vector)-1
pos=busqueda_binaria(vector,info_buscar,izq,der)
if pos==-1:
    print("Información NO encontrada")
else:
    print("Información encontrada en la posición: ",pos)
