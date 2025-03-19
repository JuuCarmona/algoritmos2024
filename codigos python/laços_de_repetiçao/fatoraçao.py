numero = int(input("Digite um número inteiro maior ou igual a 2: "))

if numero < 2:
    print("Erro: O número fornecido deve ser maior ou igual a 2.")
else:
    print(f"Fatorização do número {numero}:")
    fator = 2

    while fator <= numero:
        if numero % fator == 0:
            print(fator)
            numero = numero // fator
        else:
            fator = fator + 1
