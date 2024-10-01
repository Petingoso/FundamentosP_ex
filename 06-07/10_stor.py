def codifica(str):
    return str[::2] + str[1::2] # percorrer pares e depois impares

def descodifica(str):
    meio = len(str)//2
    impar = len(str) % 2
    r = ''
    for i in range(meio):
        # acebd 
        # a + d ; c + b; ...
        r += str[i] + str[meio + impar + i]
    return r + str[meio:meio+1] # se impar devolve meio ou lista vazia




print(codifica('abcde'))

print(descodifica('acebd'))

