#EJERCICIOS SEMANA 2
#3 TRASRAPIDO

print(" comision de 4 conductores...")
for i in range(4):
    cedula=int(input("Cedula: "))
    nombre=input("Nombre : ")
    direccion=input("Direccion : ")
    telefono=input("Telefono : ")
    clase=input("Clase de conductor (E: experto, N: novato): ")
    pasajes=float(input("Valor total por pasajes del mes: "))
    encomiendas=float(input("Valor total por encomiendas del mes: "))
    print(" ")
    if clase == "E":
        print("Comision para conductor EXPERTO:")
        copa=pasajes*0.3
        coen=encomiendas*0.2
        toco=copa+coen
        print("Nombre conductor: ", nombre)
        print("Comision pasajes: ", "{:,.2f}".format(copa))
        print("Comision encomiendas: ", "{:,.2f}".format(coen))
        print("total Comision a pagar: ", "{:,.2f}".format(toco))
    else:
        print("Comision para conductor NOVATO:")
        copa=pasajes*0.2
        coen=encomiendas*0.15
        toco=copa+coen
        print("Nombre conductor: ", nombre)
        print("Comision pasajes: ", "{:,.2f}".format(copa))
        print("Comision encomiendas: ", "{:,.2f}".format(coen))
        print("total Comision a pagar: ", "{:,.2f}".format(toco))
    print(" ")
print("...fin proceso calculo comision")
