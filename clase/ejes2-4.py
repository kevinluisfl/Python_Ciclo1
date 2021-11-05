#EJERCICIOS SEMANA 2
#4 NOTA DEFINITIVA

print("calculo de nota definitiva a 5 estudiantes...")
for i in range(5):
    codigo=int(input("Codigo: "))
    nombre=input("Nombre : ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    nota3=float(input("Nota 3: "))
    print(" ")
    notadef= (nota1*0.35) + (nota2*0.35) + (nota3*0.3)
    print("Codigo estudiante: ", codigo)
    print("Nombre estudiante: ", nombre)
    print("La nota definitiva es: ", "{:,.2f}".format(notadef))
    print(" ")
print("...fin proceso calculo nota")
