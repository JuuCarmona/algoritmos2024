numero_binario = input("Digite um número binário: ")

numero_decimal = 0
expoente = 0

for digito_binario in reversed(numero_binario):
    if digito_binario == '1':
        numero_decimal = numero_decimal + 2 ** expoente
    expoente = expoente + 1

print("O número decimal equivalente é:", numero_decimal)
