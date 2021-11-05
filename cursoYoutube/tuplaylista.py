#tuplas y listas

mitupla=("kevin",21,9,1993)
milista=list(mitupla)
print(milista)
print("kevin" in milista)
print(milista[:2])

milista2=["kevin",21,9,1993]
mitupla2=tuple(milista2)
print(mitupla2)
print(21 in mitupla2)
print(mitupla2.count(21))

nombre, dia, mes, anno = mitupla2
print(nombre)
print(anno)


