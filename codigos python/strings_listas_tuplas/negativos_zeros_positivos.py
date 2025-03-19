negativos = []
zeros = []
positivos = []

print("Digite números inteiros (pressione Enter para sair):")
while True:
    entrada = input()
    if entrada == "":
        break
    numero = int(entrada)
    if numero < 0:
        negativos.append(numero)
    elif numero == 0:
        zeros.append(numero)
    else:
        positivos.append(numero)

print("Números negativos:")
for numero in negativos:
    print(numero)

print("Zeros:")
for numero in zeros:
    print(numero)

print("Números positivos:")
for numero in positivos:
    print(numero)
