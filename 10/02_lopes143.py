def cria_rac(n, d):
    if d<=0:
        raise ValueError("argumentos errados")
    return {'n':n, 'd':d}
    
def num(r):
    return r['n']

def den(r):
    return r['d']

def eh_racional(arg):
    if num(arg)%1==0 and den(arg)%1==0 and den(arg)>0 and isinstance(arg, dict):
        return True
    else:
        return False

def eh_rac_zero(arg):
    return num(arg)==0 and eh_racional(arg)

def rac_iguais(r1, r2):
    if not (eh_racional(r1) and eh_racional(r2)):
        return True
    else:
        return num(r1)*den(r2)==num(r2)*den(r1)
    
# a)

def escreve_rac(r):
    if not eh_racional(r):
        raise ValueError
    return str(num(r))+'/'+str(den(r))

def produto_rac(r1, r2):
    if not (eh_racional(r1) and eh_racional(r2)):
        raise ValueError
    return cria_rac(num(r1)*num(r2), den(r1)*den(r2))

#print(escreve_rac(produto_rac(cria_rac(1,3), cria_rac(3,4))))

# b)