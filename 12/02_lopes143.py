def produtorio(lm_inf, lm_sup, calc_termo, proximo):
    prod=1
    while lm_inf<=lm_sup:
        prod*=calc_termo(lm_inf)
        lm_inf=proximo(lm_inf)
    return prod

def factorial(n):
    return produtorio(1, n, lambda x:x, lambda x:x+1)

#print(factorial(52))