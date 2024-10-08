def agrupa_por_chave(w):
    d = {}
    for k,v in w:
        if k in d:
            d[k].append(v)
        else:
            d[k]=[v]
