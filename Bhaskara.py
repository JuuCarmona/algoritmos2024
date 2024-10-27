import math
# Peça o valor de A
A = int(input("digite o valor de A:"))
# Peça o valor de B
B = int(input("digite o valor de B:"))
# Peça o valor de C
C = int(input("digite o valor de C:"))
# Ache o valor de delta
Delta = B * B - 4*A*C
# Se o delta for menor que 0 não tem raiz.
if Delta < 0:
    print("Não possui raíz.")
# Se o delta  for igual a 0 possui uma raiz.
elif Delta == 0:
    r1 = - B / 2*A
    print(r1)
# Se o delta for maior que 0 possui 2 raizes.
else:
    print(math.sqrt(Delta))
    r1 = (- B + math.sqrt(Delta))/(2*A)
    r2 = (- B - math.sqrt(Delta))/ (2*A)
    print(r1,r2)
