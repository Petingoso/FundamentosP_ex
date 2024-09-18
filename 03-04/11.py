input_string = input("Escreva um inteiro: ")
output_string = ""
length = len(input_string)

for i in range(1,length+1):
    output_string = output_string + input_string[length - i]
print(output_string)
