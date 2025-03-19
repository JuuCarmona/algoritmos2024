def palavras_unicas():
    palavras_digitadas = []

    while True:
        palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
        if palavra == "":
            break
        palavras_digitadas.append(palavra)

    palavras_unicas = []
    for palavra in palavras_digitadas:
        if palavra not in palavras_unicas:
            palavras_unicas.append(palavra)

    print("Palavras digitadas:")
    for palavra in palavras_unicas:
        print(palavra)

palavras_unicas()
