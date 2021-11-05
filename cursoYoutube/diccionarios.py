#diccionarios
#clave:valor

#operando diccionarios
midicio = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
midicio["Italia"]="Lisboa"
#print(midicio)
midicio["Italia"]="Roma"
#print(midicio)
del midicio["Reino Unido"]
#print(midicio)

#la clave y el valor puede ser de cualquier tipo de dato
midicio2 = {3:"Berlin","Francia":"Paris","Reino Unido":3,"España":"Madrid"}

#se puede asignar la clave o valor desde una tupla o lista
mitupla = ["Alemania","Francia","Reino Unido","España"]
midicio3 = {mitupla[0]:"Berlin",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Madrid"}
#print(midicio3["Francia"])


midicio4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997]}}
print(midicio4)
print(midicio4.keys())
print(midicio4.values())
