soma = 0 
conta = 0

valor = int(input("digite o valor:"))

if valor == 0:
    print("erro!")
else:
    soma = soma + valor
    conta = conta + 1

for i in range(1, conta + 1):
    valor_2 = int(input("digite o valor:"))
    if valor_2 == 0:
        break
soma = soma + valor_2
conta = conta + 1

if conta > 1:
    media = soma / (conta - 1)
    print("a média é:",media)
else:
    print("outro valor não foi inserido!")
