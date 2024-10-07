def agrupa_por_chave(list):
    d = {}
    for i in list:
        if i[0] in d:
            d[i[0]] += [i[1]]
        else:
            d[i[0]] = [i[1]]
    return d

print(agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)]))