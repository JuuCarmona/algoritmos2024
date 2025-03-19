import math

a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))
c = int(input("digite o valor de c:"))

if  b**2 - 4*a*c < 0:
    print("não possui raiz real")
elif  b**2 - 4*a*c == 0:
        print("apenas uma raiz")
        d = b ** 2 - 4 * a * c
        raiz_positiva = ((-1)* b + (math.sqrt(d))) / (2 * a)
        print("a raiz é:", raiz_positiva)
else:
        print("possui dua raizes reais")
        d = b** 2 - 4 * a * c
        raiz_positiva = ((-1)* b + (math.sqrt(d))) / (2 * a)
        raiz_negativa = ((-1)* b -(math.sqrt(d))) / (2 * a)
        print(f"as duas raizes são reais:{raiz_positiva,raiz_negativa}")
