#EJERCICIOS SEMANA 2
#2 SUBSIDIO VIVIENDA

print("subsidio de vivienda a 5 personas...")
ssub=0
csub=0
for i in range(5):
    nombre=input("Nombre : ")
    cedula=int(input("Cedula: "))
    ingreso=float(input("Ingreso anual promedio: "))
    personas=int(input("Personas a cargo: "))
    print(" ")
    if ingreso > 24000000 and personas >= 3:
        print("Tiene derecho al subsidio:")
        print("Nombre persona: ", nombre)
        print("Cedula persona: ", cedula)
        csub+=1
    else:
        print("No tiene derecho al subsidio:")
        ssub+=1
    print(" ")
print("Total personas con subsidio: ",csub)
print("Total personas sin subsidio: ",ssub)
print("...fin proceso calculo subsidio")
