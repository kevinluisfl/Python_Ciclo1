#Funciones (modularidad)
def factura_abonado(est,imp):
    if est==1:
        tb=10000
    elif est==2:
        tb=15000
    elif est==3:
        tb=20000
    elif est==4:
        tb=25000
    else:
        tb=30000
    vimp=imp*100
    va=tb+vimp
    return va

#Programa principal
N=int(input("Ingrese cantidad de abonados: "))
vta=0
for i in range(N):
    nom=input("Nombre: ")
    est=int(input("Estrato(1,2,3,4,5): "))
    imp=int(input("Impulsos del mes: "))
    #Llamado al módulo( función)... ejecute la función para calcular el va
    va=factura_abonado(est,imp)
    vta=vta+va
    print("Valor a pagar abonado: ",'{:,.2f}'.format(va))
print("Valor total abonados: ",'{:,.2f}'.format(vta))
