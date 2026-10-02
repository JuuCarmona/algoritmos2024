coluna = input("Digite qual a sua posição da coluna (a-h): ")
linha = int(input("Digite qual a sua posição da linha (1-8): "))

if coluna == "a" or "c" or "e" or "g":
    quadrado_preto = True
else: 
    quadrado_branco = False
if quadrado_preto:
     if linha % 2 == 0:
      quadrado = "branco" 
     else:
      quadrado = "preto"
else:
     if linha % 2 == 1:
      quadrado = "preto"
     else:
      quadrado = "branco"

print("Sua posição é:", quadrado)
