def inverter(x):
    o = 0
    while x!=0:
        dig = x%10
        x//=10
        o = o*10 + dig
    return o

def misterio(n):
    if (not isinstance(n, int)) or (not (n/1000)>0):
        raise ValueError
    ni = inverter(n)
    ns = abs(n-ni)
    nsi = inverter(ns)
    if ns+nsi == 1089:
        return 1089
    else:
        return 'Condições não verificadas'

print(misterio(246))
print(misterio(131))