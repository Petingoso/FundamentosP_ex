amount = 100*eval(input("Entra o número de €: "))

notas = [["Notas 50:", 5000],
         ["Notas 20:", 2000],
         ["Notas 10:", 1000],
         ["Notas 5:", 500],
         ["Moedas 2:", 200],
         ["Moedas 1:", 100],
         ["Moedas 50c:", 50],
         ["Moedas 25c:", 25],
         ["Moedas 10c:", 10],
         ["Moedas 5c:", 5],
         ["Moedas 2c:", 2],
         ["Moedas 1c:", 1]]

resto = amount%notas[0][1]
print(notas[0][0], amount//notas[0][1])
for value in range(1, len(notas)):
    print(notas[value][0], resto//notas[value][1])
    resto = resto%notas[value][1]  
    
