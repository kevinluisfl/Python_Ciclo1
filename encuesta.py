#Ejercicio encuentas vehiculos

N = int(input("Cuantos dias dura la encuesta?: "))

canho=0 #cantidad hombres
canmu=0 #cantidad mujeres
cantah=[] #cantidad autos  hombres
promah=0 #promedio autos hombres
cantcm=[] #cantidad camionetas mujeres
promcm=0 #promedio camionetas mujeres
homot=0 #hombres prefieren motos
mujcam=0 #mujeres prefieren camionetas
peraut=0 #cuantos prefieren autos

for i in range(N):
    print("")
    p = int(input(f"Cuantas personas se encuestan el dia {i+1}: "))
    k=1
    while k<=p:
        print(f"Dia {i+1} persona #{k}")
        gen=input("Genero, (M: masculino, ,F: femenino): ")
        opc=int(input("Escoja vehiculo (1: Moto, 2: auto, 3: camioneta): "))
        can=int(input("cuanto(a)s compraria?: "))
        if gen == "F":
            canmu+=1
            if opc == 2:
                peraut+=1
            elif opc == 3:
                cantcm.append(can)
                mujcam+=1
        elif gen == "M":
            canho+=1
            if opc == 1:
                homot+=1
            elif opc == 2:
                cantah.append(can)
                peraut+=1
        k+=1

print("")
print("...Resultados encuesta...")
print("")
print("A: Cuantos hombres y cuantas mujeres hicieron parte de la encuesta? ")
print("Hombres: ", canho)
print("Mujeres: ", canmu)
print("")
print("B: Promedio de autos que los hombres comprarian: ", sum(cantah)/len(cantah))
print("")
print("C: Promedio de camionetas que las mujeres comprarian: ", sum(cantcm)/len(cantcm))
print("")
print("D: Cuantos hombres desearian comprar moto?: ", homot)
print("")
print("E: Cuantas mujeres desearian comprar camioneta?: ", mujcam)
print("")
print("F: Cuantas personas desearian comprar auto?: ", peraut)
print("")
print("...Fin resultados encuesta...")





        
        
        
