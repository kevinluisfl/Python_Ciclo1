#JSON en python

#importar modulo
import json

#datos a ingresar
numeros=[1,4,7,9,10,5]
diccionario={
    '1':'lapiz',
    '2':'borrador',
    '3':'cuaderno',
    '4':'regla',
    5:56}

#apertura y creacion
with open("listadicc.json","w") as archivo:
    #json.dump(numeros,archivo)
    json.dump(diccionario,archivo)

#apertura y lectura
with open("listadicc.json","r") as archivo:
    datos=json.load(archivo)

#fase cierre
archivo.close()

#impresion dato de archivo JSON
#print("lista JSON",datos)
print("diccionario JSON",datos)  
