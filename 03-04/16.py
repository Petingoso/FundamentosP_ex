conjunto = [15,10,9,19,7,8] #qualquer coisa

positivas = 0

for nota in conjunto:
    if(nota>=10):
        positivas +=1
        print(nota)

percentagem = positivas/len(conjunto)
print("Houve", positivas, "positivas e houve", percentagem*100, "\b% positivas")



