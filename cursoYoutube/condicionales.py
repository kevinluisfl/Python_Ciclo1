
#anidando condiciones en if, de izquierda a derecha
edad=int(input("Ingrese edad: "))
#0<edad y despues edad<100
if  0<edad<100:
    print("La edad es correcta en el rango de 0 a 100: "+str(edad))
else:
    print("La edad esta fuera del rango de 0 a 100: "+str(edad))
#python es fuertemente tipado, toca especificar el tipo de dato y transformarlo en uno para concatenar

# AND OR
print("")
dis=int(input("Ingrese distancia (km): "))
her=int(input("Ingrese # hermanos: "))
sal=int(input("Ingrese salario anual: "))

if dis>40 and her>2 or sal<=20000:
    print("BECA!")
else:
    print("SIN BECA")

#IN
print("")
print("Asignaturas: Informatica Grafica - Fisica - Matematicas ")
opcion=input("Escriba asignatura: ")

#python es case sensitive, no distingue MAYUS de minus o acentos
asignatura=opcion.lower()

if asignatura in ("informatica grafica","fisica","matematicas"):
    print("Asignatura escogida "+opcion)
else:
    print("La asignatura no esta disponible en las opciones")


