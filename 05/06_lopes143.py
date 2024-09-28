def bissexto(x):
    if x%4==0 and (x%100!=0 or x%400==0):
        return 29
    else:
        return 28

def dias_mes(mes, ano):
    if mes=="jan" or mes=="mar" or mes=="mai" or mes=="jul" or mes=="ago" or mes=="out" or mes=="dez":
        return 31
    elif mes=="abr" or mes=="jun" or mes=="set" or mes=="nov":
        return 30
    elif mes=="fev":
        return bissexto(ano)
    else:
        raise ValueError("Mes nao existe")
    
print(dias_mes('jan', 2017))
print(dias_mes('fev', 2016))
print(dias_mes('MAR', 2017))