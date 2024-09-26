def floor(x):
    i=0
    while (i<=x):
        i+=1
    return i-1

def dia_da_semana(d,m,ano):
    if m < 3: # janeiro e fevereiro
        m += 12
        ano -= 1

    k = ano % 100
    j = floor(ano/100)
    h = (d + floor(((13*(m+1))/5)) + k + floor(k/4) + floor(j/4) - 2*j) % 7 

    dias = ("sabado","domingo","segunda","terca","quarta","quinta","sexta") # matéria "proibida"
    return dias[h]
print(dia_da_semana(18, 1, 2014))

