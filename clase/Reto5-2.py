#Reto 5: Ordenamiento de equipos por puntos
#Autor: Kevin Luis Flórez Lozada
#Fecha: 23/06/2021 

#Funcion de ordenamiento
def ordenamientoPuntos(Equipos,Abreviados,Ganados,Empatados,Perdidos,Puntos):
    for i in range (0,N-1,1):
        for j in range(i+1,N,1):
            if Puntos[i]<=Puntos[j]:
                #Equipos
                aux=Equipos[i]
                Equipos[i]=Equipos[j]
                Equipos[j]=aux
                #Abreviados
                aux=Abreviados[i]
                Abreviados[i]=Abreviados[j]
                Abreviados[j]=aux
                #Ganados
                aux=Ganados[i]
                Ganados[i]=Ganados[j]
                Ganados[j]=aux
                #Empatados
                aux=Empatados[i]
                Empatados[i]=Empatados[j]
                Empatados[j]=aux
                #Perdidos
                aux=Perdidos[i]
                Perdidos[i]=Perdidos[j]
                Perdidos[j]=aux
                #Puntos
                aux=Puntos[i]
                Puntos[i]=Puntos[j]
                Puntos[j]=aux           
    return Equipos,Abreviados,Ganados,Empatados,Perdidos,Puntos
#
#validacion numero entero
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

#abreviar nombres para tabla
Abreviados=[]
for i in range(N):
    Abreviados.append(Equipos[i][:3].upper())

#mostrar listas ingresadas
print("Listas ingresadas: ")
print("Equipos", Equipos)
print("Abreviados", Abreviados)
print("Ganados", Ganados)
print("Empatados", Empatados)
print("Perdidos", Perdidos)
print("puntos", Puntos)

#llamada a la funcion que ordena
ordenamientoPuntos(Equipos,Abreviados,Ganados,Empatados,Perdidos,Puntos)

#impresion de tabla ordenada
print("")
print("---------------------")
print("-TABLA DE POSICIONES-")
print("---------------------")
print("NOM |","G |","E |","P |","PTS")
print("---------------------")
for i in range(N):
    print(Abreviados[i],"|",Ganados[i],"|",Empatados[i],"|",Perdidos[i],"|",Puntos[i])
    print("---------------------")

print("CAMPEÓN!!!!!!!")
print("Felicitaciones a:", Equipos[0].upper(), "("+Abreviados[0]+") por ganar el campeonato con",Puntos[0], "puntos")




