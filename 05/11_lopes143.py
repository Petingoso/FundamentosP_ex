def media_digitos(n):
    num = 0
    i = 0
    while n!=0:
        dig = n % 10
        n//=10
        num += dig
        i+=1
    out = num/i
    return out

print(media_digitos())