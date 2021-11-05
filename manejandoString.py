#captura cadenas de caracteres, y por cada una imprime la primera letra, mitad y ultima en MAYUSCULA 
#tambien muestra si son palindromo


##lista
#e=['juventus','anilina','madrid','Isaac no ronca asi','barcelona','loopvevpool','parangutirimicuaro','anita lava la tina']
#print(e)
##cantidad de datos
#N=len(e) 

#funcion validacion entero
def validarInt(mensaje):
    while True:
        try:
            num=int(input(mensaje))
            break
        except ValueError:
            print("Error, inserte número entero!!")
    return num

print("INGRESE TEXTO Y COMPRUEBE SI ES PALINDROMO")
N=validarInt("Cuantos textos va a comprobar?: ")
e=[]
for i in range(N):
    dato=input(f"Texto {i+1} de {N}: ")
    e.append(dato)

print("")
print("PRIMERA, MITAD(ES) Y ULTIMA LETRA MAYUSCULAS")
print("")
for i in range(N):
    #tamaño nombre
    tn=len(e[i])
    #mitad nombre
    mn=len(e[i])//2
    #siguiente de mitad
    sm=mn+1
    #ultimo
    u=len(e[i])-1
    if len(e[i])%2==1:
        #impresion de cada nombre cantidad letras IMPARES
        nom=e[i][0].upper()+e[i][1:mn]+e[i][mn].upper()+e[i][sm:u]+e[i][u].upper()
        print(nom)
    else:
        #impresion de cada nombre cantidad letras PARES
        #se toman dos mitades
        #nueva mitad
        mn-=1
        #siguiente nuevo
        sm=mn+2
        nom=e[i][0].upper()+e[i][1:mn]+e[i][mn].upper()+e[i][mn+1].upper()+e[i][sm:u]+e[i][u].upper()
        print(nom)

print("")
print("COMPROBACIÓN DE PALINDROMOS")
print("")
#ciclo para revisar palindromo dentro de la lista
for i in range(N):
    #probar si es palindromo
    #quito espacios de la cadena y pongo todo minusculas
    ose=e[i].replace(" ","").lower()
    #inver=e[i][::-1]
    inver=ose[::-1]
    #if e[i]==inver:
    if ose==inver:
        print("Original:",e[i])
        print("Sin espacios:",ose)
        print("Invertida:",inver,", Es un palindromo!!!!!")
    else:
        print("Original:",e[i])
        print("Sin espacios:",ose)
        print("Invertida:",inver,", NO palindromo!")
    print("")

