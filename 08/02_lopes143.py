# Primeiro ponto
# Cria uma nova lista com os não-múltiplos
def remove_multiplos(lista, num):
    outLista = []
    for i in lista:
        if i%num!=0:
            outLista.append(i)
    
    return outLista

print(remove_multiplos([2, 3, 5, 9, 12, 33, 34, 45], 3))


# Segundo ponto
# Apaga os múltiplos da lista atual
def remove_multiplos_2(lista, num):
    for i in lista:
        for j in lista:
            if j%num==0:
                lista.remove(j)

    return lista

print(remove_multiplos_2([2, 3, 5, 9, 12, 33, 34, 45], 3))