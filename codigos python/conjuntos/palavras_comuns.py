texto1 = set(input("Digite o primeiro texto que deseja inserir:").split())
texto2 = set(input("digite o segundo texto que deseja inserir:").split())

comuns = texto1.intersection(texto2)
print(comuns)
