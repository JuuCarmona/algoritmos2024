numero = int(input("Digite um número decimal: "))

resultado = 0
expoente = 0
while numero > 0:
    
    bit = numero % 2
    resultado = resultado + bit * (10 ** expoente)
    numero = numero // 2
    expoente += 1

print("O número binário correspondente é:", resultado)
