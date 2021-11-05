#Reto 5: Ordenamiento de equipos por puntos
#Autor: Kevin Luis Flórez Lozada
#Fecha: 19/06/2021 

#Funcion
def ordenamientoPuntos(Equipos,Ganados,Empatados,Perdidos,Puntos):
    for i in range (0,N-1,1):
        for j in range(i+1,N,1):
            if Puntos[i]<=Puntos[j]:
                #Equipos
                ne=Equipos[i]
                Equipos[i]=Equipos[j]
                Equipos[j]=ne
                #Ganados
                pg=Ganados[i]
                Ganados[i]=Ganados[j]
                Ganados[j]=pg
                #Empatados
                pe=Empatados[i]
                Empatados[i]=Empatados[j]
                Empatados[j]=pe
                #Perdidos
                pp=Perdidos[i]
                Perdidos[i]=Perdidos[j]
                Perdidos[j]=pp
                #Puntos
                pt=Puntos[i]
                Puntos[i]=Puntos[j]
                Puntos[j]=pt           
    return Equipos,Ganados,Empatados,Perdidos,Puntos
#
#entero
def validarInt(mensaje):
    while True:
        try:
            num=int(input(mensaje))
            break
        except ValueError:
            print("Error de dato, debe ser un número entero!")
    return num
#

#Principal
N=validarInt("Ingrese cantidad EQUIPOS participantes: ")
print("")
Equipos=[]
Ganados=[]
Empatados=[]
Perdidos=[]
Puntos=[]
for i in range(N):
    Nomequipos= input("Ingrese NOMBRE de equipo(NOM): ")
    Equipos.append(Nomequipos)
    
    NGanados=validarInt("Ingrese Numero de partidos GANADOS: ")
    Ganados.append(NGanados)
    
    NEmpatados=validarInt("Ingrese Numero de partidos EMPATADOS: ")
    Empatados.append(NEmpatados)
    
    NPerdidos=validarInt("Ingrese Numero de partidos PERDIDOS: ")
    Perdidos.append(NPerdidos)
    print("")
    puntosEqu=(NGanados*3)+(NEmpatados*1)
    Puntos.append(puntosEqu)

print("Listas ingresadas: ")
print("Equipos", Equipos)
print("Abreviados", Abreviados)
print("Ganados", Ganados)
print("Empatados", Empatados)
print("Perdidos", Perdidos)
print("puntos", Puntos)

Ordenados= ordenamientoPuntos(Equipos,Ganados,Empatados,Perdidos,Puntos)
#print("Tabla de puntos: ", Ordenados)
print("")
print("---------------------")
print("-TABLA DE POSICIONES-")
print("---------------------")
#cabecera=["NOM","G","E","P","PTS"]
#print(cabecera[0],"|",cabecera[1],"|",cabecera[2],"|",cabecera[3],"|",cabecera[4])
print("NOM |","G |","E |","P |","PTS")
print("---------------------")
for i in range(N):
    #nomEquipo=Equipos[i]
    #Equipos[i][:3].upper()
    print(Equipos[i][:3].upper(),"|",Ganados[i],"|",Empatados[i],"|",Perdidos[i],"|",Puntos[i])
    print("---------------------")




