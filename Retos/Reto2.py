#Reto 2
#Programa para calcular valor a pagar por estudiante
#Autor: Kevin Luis Florez Lozada
#Fecha: 24/5/2021

print("...Registro nueva matricula")
codigo=int(input("codigo del estudiante: "))
while codigo!=999:
    nombre=input("Nombre estudiante: ")
    print("-----Costo matricula------")
    print("(1)Técnico en Sistemas: $800.000")
    print("(2)Técnico en Desarrollo de videojuegos: $1'000.000")
    print("(3)Técnico en Animación Digital: $1'200.000")
    progracam=int(input("Ingrese codigo del programa academico: "))
    if progracam==1:
        valormatricula=800000
        promat="Técnico en Sistemas"
    elif progracam==2:
        valormatricula=1000000
        promat="Técnico en Desarrollo de videojuegos"
    else:
        valormatricula=1200000
        promat="Técnico en Animación Digital"
    print("------% Descuento por Beca--------")
    print("(1)Beca por rendimiento académico. Descuento del 50%")
    print("(2)Beca Cultural – Deportes. Descuento del 40% ")
    print("(3)Sin Beca. Descuento 0%")
    beca=int(input("Ingrese codigo de beca: "))
    if beca==1:
        porcbeca=0.5
        tbec="Rendimiento académico"
    elif beca==2:
        porcbeca=0.4
        tbec="Beca Cultural – Deportes"
    else:
        porcbeca=0
        tbec="No aplica"
    valorbeca=valormatricula*porcbeca
    matriculaneta=valormatricula-valorbeca
    print("")
    print("------------Resultado----------------")
    print("El estudiante de codigo: ",codigo)
    print("Nombre estudiante: ",nombre)
    print("Programa matriculado fue: ", promat)
    print("Valor matricula: ",'{:,}'.format(valormatricula))
    print("La beca aplicada fue: ",tbec)
    print("Valor beca: ",'{:,}'.format(valorbeca))
    print("Total a pagar: ",'{:,}'.format(matriculaneta))
    print("Fin registro...")
    print("")
    print("...Registro nueva matricula")
    codigo=int(input("codigo del estudiante: "))
print("Fin registro por codigo prohibido: ",codigo)
