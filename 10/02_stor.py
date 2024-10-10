def produto_rac(r1,r2):
    return cria_rac(num(r1)*num(r2),den(r2)*den(r1))

def escreve_rac(r):
    return str(num(r))+'/'+str(den(r))

def cria_rac(n,d):
    if (type(d) is not int) or d<=0:
        raise ValueError("Erro denominador")
    if (type(n) is not int):
        raise ValueError("Erro numerador")
    return{'n':n,'d':d}

def rac_iguais(r1,r2):
    return num(r1)*den(r2) == num(r2)*den(r1)


def num(r):
    return r['n']

def den(r):
    return r['d']

def eh_racional(arg):
    if type(arg) is not dict or len(arg) !=2:
        return False
    
    if ('n' not in arg) or ('d' not in arg):
        return False

    n,d = arg['n'],arg['d']

    return (type(n) is int) and (type(d) is int and d>0)

def eh_rac_zero(r):
    return r['n'] == 0

