#EJERCICIOS SEMANA 2
#1 MERCADEO POPULAR

print("calculo de comision a 5 vendedores...")
for i in range(5):
    nombre=input("Nombre : ")
    tipo=int(input("tipo vendedor (1: Mayorista, 2: Minorista): "))
    ventas=float(input("Total ventas realizadas: "))
    if tipo==1:
        comision=ventas*0.25
    else:
        comision=ventas*0.15
    print(" ")
    print("la comision para el vendedor es: ","{:,}".format(comision))
print("...fin proceso calculo comision")
