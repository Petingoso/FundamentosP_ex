def cria_rel(h,m,s):
    if h<0 or m<0 or s<0 or type(h)!=int or type(m)!=int or type(s)!=int:
        raise ValueError("cria_rel: argumentos errados")
    return {'h':h, 'm':m, 's':s}

def horas(r):
    return r['h']

def minutos(r):
    return r['m']

def segundos(r):
    return r['s']

def eh_relogio(arg):
    if horas(arg)%1==0 and minutos(arg)%1==0 and segundos(arg)%1==0 and horas(arg)<24 and minutos(arg)<60 and segundos(arg)<60:
        return True
    else:
        return False

def eh_meia_noite(arg):
    if horas(arg)==minutos(arg)==segundos(arg)==0:
        return True
    else:
        return False
    
def eh_meio_dia(arg):
    if horas(arg)==12 and minutos(arg)==segundos(arg)==0:
        return True
    else:
        return False

def mesmas_horas(r1, r2):
    if horas(r1)==horas(r2) and minutos(r1)==minutos(r2) and segundos(r1)==segundos(r2):
        return True
    else:
        return False

#a)

def depois_rel(r1, r2):
    if horas(r2)>horas(r1):
        return True
    elif horas(r2)==horas(r1):
        if minutos(r2)>minutos(r1):
            return True
        elif minutos(r2)==minutos(r1):
            if segundos(r2)>segundos(r1):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#b)
    
def dif_segs(r1, r2):
    if (horas(r2)*3600+minutos(r2)*60+segundos(r2))-(horas(r1)*3600+minutos(r1)*60+segundos(r1))<0:
        raise ValueError("dif_segs: primeiro arg posterior ao segundo")
    else:
        return ((horas(r2)*3600+minutos(r2)*60+segundos(r2))-(horas(r1)*3600+minutos(r1)*60+segundos(r1)))
    
#c)
def relogio_list(h, m, s):
    return [h,m,s]

#d)
def escreve_relogio(arg):
    return f"{horas(arg):02}:{minutos(arg):02}:{segundos(arg):02}"

#e) Chamar os valores do relógio por ['horas'] / ['min'] / ['seg '] em vez de [0] / [1] / [2]

