#ordenamiento de vector 

#funciones
def ordenamiento_burbuja(vector):
    for i in range(0,N-1,1):
        for j in range(i+1,N,1):
            if vector[i]>=vector[j]:
                t=vector[i]
                vector[i]=vector[j]
                vector[j]=t
    return vector

#Programa principal
N=int(input("Cantidad de elementos: "))
vector=[]
for i in range(N):
    num=int(input("Ingrese número: "))
    vector.append(num)
print("Lista inicial: ",vector)
vector=ordenamiento_burbuja(vector)
print("Lista ordenada: ", vector)
