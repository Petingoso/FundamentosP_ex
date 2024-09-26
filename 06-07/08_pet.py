#outra alternativa e percorrer com nested loop (por cada elemento de 2 percorrer 1)
#ou juntar num tuple e fazer sort (lol)

def junta_ordenados(tup1, tup2):
    result = ()
    i = j = 0
    
    while i < len(tup1) and j < len(tup2): # nao passar a lista pequena
        if tup1[i] <= tup2[j]:
            result+= (tup1[i],)
            i += 1
        else:
            result+= (tup2[i],)
            j += 1
    
    # Append any remaining elements from either tuple
    result+= (tup1[i:])
    result+= (tup2[j:])
    
    return result

# Test the function
print(junta_ordenados((2, 34, 200, 210), (2, 230)))


