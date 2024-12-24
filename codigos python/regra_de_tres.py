def regra_de_tres(a, b, c):
    # se o valor de a for 0
    if a == 0:
        return "O valor de 'a' não pode ser zero."
    # calcule o valor de d
    d = (b * c) / a
    return d
# peça ao usuário a , b , c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
# mostre o resutado
resultado = regra_de_tres(a, b, c)
print("o valor de d é:",resultado)
