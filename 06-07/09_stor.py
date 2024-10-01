def reconhece(str):
    if str and str[0] in 'ABCD' and str[-1] in '1234': # if str checa se não é vazio
        i = 1

        #para quando chega aos numeros, que sabemos existirem
        while str[i] in 'ABCD': 
            i +=1 
        while i<len(str) and str[i] in '1234': # parar no final
            i+=1

        # se nao percorreu todos e saiu mais cedo é falso   
        return i == len(str) 
    return False

print(reconhece('A1'))
print(reconhece('ABBBBCDDDD23311'))
print(reconhece('ABC12C'))

