total = 0

while True:
    idade_1 = input("Digite a idade da pessoa (ou deixe em branco para terminar): ")
    if idade_1== "":
        break
    idade = int(idade_1)
    if idade <= 2:
        total = total + 0
    elif 3 <= idade <= 12:
        total = total + 14.00
    elif idade >= 65:
        total =total + 18.00
    else:
        total = total +23.00

print(f"O preço total é: R$ {total:.2f}")
