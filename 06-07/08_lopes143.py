def junta_ordenados(t1, t2):
    n1 = n2 = 0
    tfinal = ()
    while n1!=len(t1) and n2!=len(t2):
        if t1[n1] < t2[n2]:
            tfinal += (t1[n1], )
            n1 += 1
        elif t1[n1] >= t2[n2]:
            tfinal += (t2[n2], )
            n2 += 1
    # o while pára quando esgotar o tuplo mais pequeno
        
    tfinal += (t1[n1:]) #juntar o restante do tuplo 1
    tfinal += (t2[n2:]) #juntar o restante do tuplo 2
    return tfinal

print(junta_ordenados((2, 34, 200, 210), (1, 23)))