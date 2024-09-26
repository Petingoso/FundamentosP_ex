def num_para_seq_cod(n):
    t = ()
    while n:
        d = n%10
        if (d%2 == 0):
            t = ((d+2)%10,) + t # mod 10 para 10 -> 0 9 -> 1
        else:
            t = ((d-2)%10,) + t
        n//=10
    return t

print(num_para_seq_cod((1234567890)))
