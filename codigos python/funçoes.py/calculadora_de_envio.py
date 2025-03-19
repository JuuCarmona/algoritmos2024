def calculadora(quantidade):
    primeiro_item = 10.95
    demais_itens = 2.95

    if quantidade >1:
        soma = primeiro_item + demais_itens * (quantidade - 1)
    else:
        soma = primeiro_item
    return soma

def main():
    quantidade = int(input("digite a quantidade de itens:"))
    soma = calculadora(quantidade)

    print("o custo de envio é:", soma)
main()
