x = float(input("Digite o valor de x: "))

raiz = x / 2
ep = 0.0001

while abs(raiz * raiz - x) > ep:
    raiz = (raiz + x / raiz) / 2

print("A raiz quadrada de", x, "é aproximadamente", raiz)
