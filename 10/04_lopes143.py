def cria_data(d,m,a):
    if type(d)==type(m)==type(a)==int and d%1==m%1==0 and 0<d<=31 and 0<m<=12:
        return (d, m, a)
    else:
        raise ValueError("cria_data: argumentos invalidos")

def dia(dt):
    return ['d']

def mes(dt):
    return ['m']

def ano(dt):
    return ['a']

def eh_data(arg):
    if len(arg)==3 and type(d)==type(m)==type(a)==int and d%1==m%1==0 and 0<d<=31 and 0<m<=12
    