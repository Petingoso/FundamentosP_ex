def soma_fn(n, fn):
    soma=0
    valorInf=1
    for i in range(1, n+1):
        soma+=fn(valorInf)
        valorInf+=1
    return soma

print(soma_fn(4, lambda x:x*x))
print(soma_fn(4, lambda x:x+1))