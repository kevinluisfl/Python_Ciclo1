# Fecha: 29/05/2021
# Nombre: Elkin Itamar Velasco Sánchez
# Programa: Liquidación matricula
cod= int(input(("ingrese Código: ")))
while cod!=999:
    nom= input("ingrese Nombre: ")
    pa= int(input("seleccione programa académico al cual pertenece: [1] Técnico en sistemas [2] Técnico desarollo videojuegos [3] Técnico animacion digital: "))
    ib= int(input("seleccione indicador de beca [1] beca rendimiento académico [2] beca cultural deportes [3] sin beca: "))
    if pa==1:
        ts=800000
        if ib==1:
            md=ts*0.5
            vtp=ts-md
        elif ib==2:
            md=ts*0.4
            vtp=ts-md
        else:
            md=ts*0
            vtp=ts-md
        print("Valor matricula programa académico sin descuento es 1: ",md)
        print("Valor total a pagar 1: ",vtp)
        print("Valor Matricula Técnico en sistema 1: ",ts)
    elif pa==2:
        ts=1000000
        if ib==1:
            md=ts*0.5
            vtp=ts-md
        elif ib==2:
            md=ts*0.4
            vtp=ts-md
        else:
            md=ts*0
            vtp=ts-md
        print("Valor matricula programa académico sin descuento es 2: ",md)
        print("Valor total a pagar 2: ",vtp)
        print("Valor Matricula Técnico en sistema 2: ",ts)
    else:
        ts=1200000
        if ib==1:
            md=ts*0.5
            vtp=ts-md
        elif ib==2:
            md=ts*0.4
            vtp=ts-md
        else:
            md=ts*0
            vtp=ts-md
        print("Valor matricula programa académico sin descuento es 3: ",md)
        print("Valor total a pagar 3: ",vtp)
        print("Valor Matricula Técnico en sistema 3: ",ts)
    cod= int(input(("ingrese Código: ")))
