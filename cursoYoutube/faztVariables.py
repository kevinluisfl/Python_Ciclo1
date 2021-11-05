#FAZT
##Variables
##!declarar varias en una linea
x,book=100,"mi libro"
print(x)
print(book)

##legibility
bookname=""
###conventiones
book_name = "libro" #Snake case
bookName = "libro" #Camel case
BookName = "libro" #Pascal case

##Constantes
##!en MAYUS para identificar
PI=3.1416
MY_NAME="kevin luis"

stri="bIg bOss"
#print(dir(stri)) #muestra los metodos de string 
print(stri.capitalize())
print(stri.swapcase())
print(stri.replace("bIg","smAll"))
print(stri.count('g'))
print(stri.find('g'))
print(stri.split())
print(stri.index('s'))
print(stri.isnumeric())
print(stri.isalpha())
print(stri[4])

print("")
name="kevin florez"
print("My name is "+name)
print("My name is {0}".format(name))
print(f"My name is {name}") #desde versión 3.6+
print("")
names=["kevin florez","jeffar saurith","pepito perez","juancho polo"]
print(names)
nombres=[]
apellidos=[]
##esto estaria dentro del for
#cortad=name.split(' ')
#nombres.append(cortad[0])
#apellidos.append(cortad[1])
#print(cortad)
for i in range(len(names)):
    cortad=names[i].split(' ')
    nombres.append(cortad[0])
    apellidos.append(cortad[1])
#
print(nombres)
print(apellidos)
#utilizaria una funcion para ordenar por nombres o apellidos
