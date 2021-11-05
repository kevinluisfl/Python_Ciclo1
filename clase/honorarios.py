

cod=int(input("codigo: "))
while cod!=999:
    nom=input("nombre: ")
    cate=int(input("categoria(1,2,3): "))
    horas=float(input("horas laboradas: "))
    if cate==1:
        honorarios=horas*35000
    elif cate==2:
        honorarios=horas*40000
    else:
        honorarios=horas*50000
    print("honorarios: ",'{:,.2f}'.format(honorarios))
    cod=int(input("codigo: "))
print("proceso finalizado")
