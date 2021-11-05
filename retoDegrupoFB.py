#CODIGO COMPLETAMENTE COPIADO
#ES UNA RESPUESTA A UN PROBLEMA PUESTO EN UN GRUPO DE FACEBOOK

usch=[
    [],
    ["17:00","18:00","19:00"],
    ["17:00","18:00","19:00"],
    ["17:00"],
    ["17:00","18:00","19:00"],
    ["17:00","18:00","19:00"],
    []
]

result=[]
hours=[]

for x in range(0,len(usch)):
    if len(usch[x])>0:
        for h in usch[x]:
            if h not in hours:
                hours.append(h)
                result.append({"hour": h, "days":[]})
            for r in result:
                if r["hour"]==h:
                    r["days"].append(x)

print(result)
