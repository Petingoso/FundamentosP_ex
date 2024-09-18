print("Escreva um número de segundos.\n Números negativos terminam.")

while True:
    segundos = eval(input("Número?: "))
    if (segundos<0):
        break
    print("São", segundos/86400, "dias")

print("Adeus")
