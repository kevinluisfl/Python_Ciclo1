#ejercicio de un vector de N elementos, buscar un item
#y devolver su posicion
#busqueda lineal

def buscaPosicion(vector,it):
    aux=0
    for i in range(N):
        if vector[i]==it:
            #return i
            pos=i
            aux=1
            #con este return devuelve el primero que encuentre
            #en caso que existan varios
            return pos
        elif aux==0:
            pos="no"
    #return -1
    return pos

N=int(input("Cantidad de elementos de la lista: "))
vector=[]

for i in range(N):
    elem=input(f"ingrese item de posicion {i} del vector: ")
    vector.append(elem)
print("")
it=input("item a buscar: ")
print("")
print("El vector ingresado es:")
print(vector)
print("")

pos=buscaPosicion(vector,it)
if pos=="no":
    print("posicion no encontrada")
else:
    print(f"La posicion del item {it} es: ", pos)
    


