def seq_racaman(n):
    termos = [0]
    # verificar termo anterior > n 
    # se (termo anterior - n) não apareceu 
    # nesse caso é (n-1) - n 
    # caso contrário é n(-1)+n
    if n == 0:
        return termos 

    for i in range(1,n): #saltar 0 pois 0->0
        termo_ant = termos[-1]

        if ((termo_ant)-i not in termos) and (termo_ant > i):
            termos.append(termo_ant-i)
        else:
            termos.append(termo_ant+i)

    return termos 

print(seq_racaman(15))
