from math import floor 

def dia_da_semana(d,m,ano):
    ano -= (m<3)
    m = (m) + 10*(m<=2) + 2*(m==1)+(m==2)
    k = ano % 100
    j = floor(ano/100)
    h = (d + floor(((13*(m+1))/5)) + k + floor(k/4) + floor(j/4) - 2*j) % 7 
    if h == 0:
        return "sabado"
    if h == 1:
        return "domingo"
    if h == 2:
        return "segunda"
    if h == 3:
        return "terca"
    if h == 4:
        return "quarta"
    if h == 5:
        return "quinta"
    if h == 6:
        return "sexta"
print(dia_da_semana(18, 2, 2014))

