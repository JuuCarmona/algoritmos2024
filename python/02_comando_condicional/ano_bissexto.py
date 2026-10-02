ano = int(input("digite um ano:"))

if ano % 400 == 0:
    print(ano,"é um ano bissexto.")
elif ano % 100 == 0:
    print(ano,"não é um ano bissexto.")
elif ano % 4 == 0:
    print(ano,"é um ano bissexto.")
else:
    print(ano,"não é um ano bissexto.")
