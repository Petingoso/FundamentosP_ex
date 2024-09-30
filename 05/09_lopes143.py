import math

def dia_da_semana(d, m, a):
    if m==1:
        mes=13
    elif m==2:
        mes=14
    expr = math.floor((d + math.floor((13*(mes+1))/5) + (a%100) + math.floor((a%100)/4) + math.floor((a/100)/4) -2*(a/100))%7)
    if expr==0:
        return 'sabado'
    elif expr==1:
        return 'domingo'
    elif expr==2:
        return 'segunda'
    elif expr==3:
        return 'terça'
    elif expr==4:
        return 'quarta'
    elif expr==5:
        return 'quinta'
    elif expr==6:
        return 'sexta'
    else:
        raise ValueError

print(dia_da_semana(18, 1, 2014))