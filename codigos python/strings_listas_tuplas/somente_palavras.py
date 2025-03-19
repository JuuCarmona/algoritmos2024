def extrair_palavras(texto):
    pontuacao = "!()-[]{};:'\"\,<>./?@#$%^&*_~"

    for p in pontuacao:
        texto = texto.replace(p, " ")

    palavras = texto.split()

    return palavras

def main():
    texto = "olá, como você está?"
    palavras = extrair_palavras(texto)
    print(palavras)

if __name__ == "__main__":
    main()
