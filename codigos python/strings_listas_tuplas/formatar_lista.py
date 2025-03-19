def formatar_lista(lista):
    tamanho = len(lista)

    if tamanho == 0:
        return ""
    elif tamanho == 1:
        return lista[0]
    elif tamanho == 2:
        return lista[0] + " e " + lista[1]
    else:  
        formatados = ", ".join(lista[:-1])
        texto_formatado = ""
        for item in lista[:-1]:
            texto_formatado += item + ", "
        texto_formatado += "e " + lista[-1]

        return texto_formatado

def main():
    lista1 = ["maçãs"]
    lista2 = ["maçãs", "laranjas"]
    lista3 = ["maçãs", "laranjas", "bananas"]
    lista4 = ["maçãs", "laranjas", "bananas", "amoras"]

    print(formatar_lista(lista1))
    print(formatar_lista(lista2))
    print(formatar_lista(lista3))
    print(formatar_lista(lista4))

if __name__ == "__main__":
    main()
