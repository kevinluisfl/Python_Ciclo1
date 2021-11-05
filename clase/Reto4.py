#Reto 4: Calculo tarifa servicio N suscriptores
#Autor: Kevin Luis Flórez Lozada
#Fecha: 09/06/2021

#Funciones
#entero
def validarInt(mensaje):
    while True:
        try:
            num=int(input(mensaje))
            break
        except ValueError:
            print("Error de dato, debe ser un número entero!")
    return num
#
#float
def validarFloat(mensaje):
    while True:
        try:
            lect=float(input(mensaje))
            break
        except ValueError:
            print("Error de dato, debe ser un número!")
    return lect
#
#estrato
def validarEst(mensaje):
    while True:
        try:
            est=int(input(mensaje))
            if est<1 or est>5:
                print("Atención! el estrato debe estar entre 1 y 5...")
                continue
            break
        except ValueError:
            print("Error de dato, debe ser un número entero!")
    return est
#
#calculos
def valorServicio(est,lmact,lmant):
    if est==1:
        tb=20000
    elif est==2:
        tb=30000
    elif est==3:
        tb=45000
    elif est==4:
        tb=60000
    else:
        tb=80000
    vcon=(lmact-lmant)*500
    vps=tb+vcon
    return vps
#

#Principal
print("Inicio programa calculo servicio...")
N=validarInt("Ingrese CANTIDAD de suscriptores: ")
print("")
vtsa=0
for i in range (N):
    nom=input("Nombre SUSCRIPTOR: ")
    est=validarEst("-Ingrese el ESTRATO (1,2,3,4 o 5): ")
    lmact=validarFloat("-Lectura mes ACTUAL en cm3: ")
    lmant=validarFloat("-Lectura mes ANTERIOR en cm3: ")
    vpsa=valorServicio(est,lmact,lmant)
    vtsa=vtsa+vpsa
    print("Valor servicio agua: ", '{:,.2f}'.format(vpsa))
    print("")
print("Valor total servicios: ", '{:,.2f}'.format(vtsa))
print("...fin programa calculo servicio")
#
