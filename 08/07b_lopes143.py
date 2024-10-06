def seq_racaman(number):
    sequence = [0]
    for n in range(1, number):
        if sequence[-1]>n and sequence[-1]-n not in sequence:
            sequence.append(sequence[-1]-n)
        else:
            sequence.append(sequence[-1]+n)
    
    return sequence

print(seq_racaman(15))
