#for else, se ejecuta lo del else cuando no usa el break

numeros = [1, 2, 4, 3, 5, 8, 6]
ite = 9
for n in numeros:
    if n == ite:
        print(f'Encontrado el {ite}')
        break
else:
    print(f'No se encontró el número {ite}')
