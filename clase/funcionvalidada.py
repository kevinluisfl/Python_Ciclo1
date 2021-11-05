#Funciones
def valida_estrato():
    while True:
        try:
            est = int(input("Ingrese Estrato(1,2 o 3) : "))
            if est<1 or est>3:
                print("Error! Estrato es 1,2 o 3. Intenta de nuevo...")
                continue
            break
        except ValueError:
            print("Error! Debe ser entero Intenta de nuevo...")
    return est

def calculo_valor_servicio(est,imp):
    if est==1:
        tb=20000
    elif est==2:
        tb=40000
    else:
        tb=50000
    vs=tb+imp*100
    return vs

#Programa principal
N=int(input("Ingrese Cantidad de abonados: "))
vts=0
for i in range (N):
    nom=input("Nombre: ")
    est=valida_estrato()
    imp=int(input("Cantidad de impulsos: "))
    vs=calculo_valor_servicio(est,imp)
    vts=vts+vs
    print("Valor Servicio: ", '{:,.2f}'.format(vs))
print("Valor total servicio: ",'{:,.2f}'.format(vts))
