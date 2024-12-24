# Função para desenhar o retângulo
def retangulo(altura, largura):
    for i in range(altura):
        for j in range(largura):
            if i == 0 or i == altura - 1:
                if j == 0 or j == largura - 1:
                    print("+", end="")
                else:
                    print("-", end="")
            else:
                if j == 0 or j == largura - 1:
                    print("|", end="")
                else:
                    print(" ", end="")
        print()

# Peça ao usuário a altura e a largura
altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))

# Desenhe o retângulo
retangulo(altura, largura)
