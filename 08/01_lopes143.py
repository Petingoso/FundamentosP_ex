def lista_codigos(inLista):
    outLista = []
    for i in inLista:
        outLista.append(ord(i))
    
    return outLista

print(lista_codigos('bom dia'))