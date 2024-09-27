def num_para_seq_cod(n):
    t = ()
    while n!=0:
        d = n%10
        n//=10
        if d%2==0:
            if d==8:
                t = (0, ) + t
            else:
                t = ((d+2), ) + t
        else:
            if d==1:
                t = (9, ) + t
            else:
                t = ((d-2), ) + t
    return t

print(num_para_seq_cod(1234567890))