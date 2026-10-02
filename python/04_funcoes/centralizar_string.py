def centralizar(texto, largura):
    espaços = largura - len(texto)
    if espaços <= 0:
        return texto
    espaços_esquerda = espaços // 2
    espaços_direita = espaços - espaços_esquerda
    return ' ' * espaços_esquerda + texto +' ' * espaços_direita

def main():
    texto = input("Digite a string a ser centralizada: ")
    largura = int(input("Digite a largura da linha do terminal em caracteres: "))
    texto_centralizado = centralizar(texto, largura)
    print("Texto:")
    print(texto_centralizado)

if __name__ == "__main__":
    main()
