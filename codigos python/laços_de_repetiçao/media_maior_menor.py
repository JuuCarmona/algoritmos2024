soma = 0
conta = 0

while conta < 10:
    numero =int(input("digite um número:"))
    soma = soma + numero

    if conta == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    conta = conta + 1

    media = soma / 10

print("média",media)
print("maior número",maior)
print("menor número",menor)
