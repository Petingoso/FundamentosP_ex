input_string = input("Escreva um inteiro: ")
output_string = ""

for i in input_string:
    if(eval(i) % 2 != 0):
        output_string = output_string + i

print(output_string)

