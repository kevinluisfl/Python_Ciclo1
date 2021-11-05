rep=int(input("Cuantos empleados va registrar?: "))

for i in range(rep):
    print("Registro #",i+1)
    #print(f"numero {i+1}")
    nombre=input("escriba el nombre: ")
    ventas=float(input("escriba las ventas: "))
    com=ventas*0.25
    print("la comision para el vendedor ",nombre," es: ",'{:,.2f}'.format(com))
print("Registros finalizados..")
