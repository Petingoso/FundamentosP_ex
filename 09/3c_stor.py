def distribui(b,n):
    if len(b)%n ==0:
        # maneira diferente de distribuir, pq nao 
        # da uma carta a cada jogador até acabarem
        return {b[i::n] for i in range(n)}
    raise ValueError('...')
