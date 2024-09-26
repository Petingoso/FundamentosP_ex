def misterio(n):
    if isinstance(n,int) and 99<n<1000 and abs(n%10-n//100)>1:
        ni = (n%10)*100 + ((n%100)//10)*10 + (n//100)
        ns = abs(n-ni)
        nsi = (ns%10)*100 + ((ns%100)//10)*10 + (ns//100)
        return ns +nsi 
    raise ValueError("misterio: argumento invalido")
