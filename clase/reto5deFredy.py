#Programa: Reto 5
#Autor: Freddy Beltran
#Fecha: 23/06/2021

def ordenamiento_puntos(Equipo,Ganados,Empatados,Perdidos,Puntos):
    for i in range (0,N-1,1):
        for j in range(i+1,N,1):
            if Puntos[i]<=Puntos[j]:
                #Equipos
                e=Equipo[i]
                Equipo[i]=Equipo[j]
                Equipo[j]=e
                #Ganados
                g=Ganados[i]
                Ganados[i]=Ganados[j]
                Ganados[j]=g
                #Empatados
                ee=Empatados[i]
                Empatados[i]=Empatados[j]
                Empatados[j]=ee
                #Perdidos
                p=Perdidos[i]
                Perdidos[i]=Perdidos[j]
                Perdidos[j]=p
                #Puntos
                t=Puntos[i]
                Puntos[i]=Puntos[j]
                Puntos[j]=t
                
    return Equipo,Ganados,Empatados,Perdidos,Puntos
print("***Bienvenido al torneo internacional de fútbol***")
N=int(input("Ingrese cantidad equipos a competencia: "))
Equipo=[]
Ganados=[]
Empatados=[]
Perdidos=[]
Puntos=[]
for i in range(N):
    Nom_equipos= input("Ingrese el nombre del equipo: ")
    Equipo.append(Nom_equipos)
    N_Ganados=int(input("Ingrese el número de partidos ganados: "))
    Ganados.append(N_Ganados)
    N_Empatados=int(input("Ingrese el número de partidos empatados: "))
    Empatados.append(N_Empatados)
    N_Perdidos=int(input("Ingrese el número de partidos perdidos: "))
    print("")
    Perdidos.append(N_Perdidos)
    puntos_equ=(N_Ganados*3)+(N_Empatados*1)
    Puntos.append(puntos_equ)

 

print("")
print("Nombre de los equipos en competencia: ", *Equipo)
print("Número total de partidos ganados de cada equipos: ", *Ganados)
print("Número total de partidos empatados de cada equipos: ", *Empatados)
print("Número total de partidos perdidos de cada equipos: ", *Perdidos)
print("Número total de puntos obtenidos por cada equipo: ", *Puntos)
ordenamiento_puntos(Equipo,Ganados,Empatados,Perdidos,Puntos)
print("")
print("***AHORA VEAMOS LA TABLA DE POSICIONES***")
print("")
p=[]
for i in range (N):
    ##en un paso
    #p.append([Equipo[i],Ganados[i],Empatados[i],Perdidos[i],Puntos[i]])
    ##en dos pasos
    p.append([])
    p[i]=[Equipo[i],Ganados[i],Empatados[i],Perdidos[i],Puntos[i]]
    
print(p)
print ("{:^10} {:^5} {:^5} {:^5} {:^8}".format('Equipo','PG','PE','PP','Puntos'))
#{:<10} to left
#{:>10} to right
#{:^10} to center
for f in p:
    Equipo,Ganados,Empatados,Perdidos,Puntos = f
    
    print ("{:<10} {:<5} {:<5} {:<5} {:<8}".format(Equipo,Ganados,Empatados,Perdidos,Puntos))
