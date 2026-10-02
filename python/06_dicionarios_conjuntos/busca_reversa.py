def buscaReversa(dicionario, valor):
    chaves_encontradas = []
    for chave, i in dicionario.items():
        if i == valor:
            chaves_encontradas.append(chave)
    return chaves_encontradas

def main():
    dicionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
    valor = 1
    chaves = buscaReversa(dicionario, valor)
    if chaves:
        print(f"As chaves associadas ao valor {valor} são: {chaves}")
    else:
        print(f"Nenhuma chave encontrada para o valor {valor}")

if __name__ == "__main__":
    main()
