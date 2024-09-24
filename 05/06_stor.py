def bissexto(m):
    return m%4==0 and (m%400 == 0 or m%100!=0)


def dias_mes(mes,ano):
    dias30=(mes == "abr" or mes =="jun" or mes =="set" or mes =="nov")
    if dias30 or mes=="jan" or mes=="fev" or mes=="mar" or mes=="mai" or mes== "jul" or mes=="ago" or mes=="out" or mes=="dez":
        return 28 + (mes=="fev" and bissexto(ano)) + (mes !="fev") * (3-dias30)

    raise ValueError("mes invalido")

