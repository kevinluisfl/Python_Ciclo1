#otra forma de llenar una matriz

N=2
nombres=[]
direcciones=[]
telefonos=[]
for i in range(N):
    nombre=input("nombre: ")
    nombres.append(nombre)
    
    direccion=input("direccion: ")
    direcciones.append(direccion)
    
    telefono=input("telefono: ")
    telefonos.append(telefono)

datos=[]
for i in range(N):
    ##directo, corchete para pasar varios datos en append
    datos.append([nombres[i],direcciones[i],telefonos[i]])
    ##en dos pasos
    #datos.append([])
    #datos[i]=[nombres[i],direcciones[i],telefonos[i]]

print(datos)
