# Exercício 1 - Par ou ímpar

número = int(input("digite um número:"))

if número % 2 == 0 :
    print(f"{número} é um número par")
else:
    print(f"{número} é um número ímpar")

# Exercício 2 - Idade canina

idade_canina = int(input("digite a idade do seu cão: "))

if idade_canina<0:
    print("o número n pode ser negativo")
elif idade_canina <= 2:
    total = idade_canina*10.5
    print("idade canina:",total)
else:
     total = (idade_canina-2)*4 + (2* 10.5)
     print("idade canina:",total)

# Exercício 3 - Vogal ou consoante

letra =input("digite uma letra: ")

if letra in ['a','e','i','o','u']:
        print(f"{letra} é uma vogal")
else: 
        print(f"{letra} é uma consoante")

# Exercício 4 - Polígono regular

poligono = int(input("digite a quantidade de lados: "))

if 3 <= poligono <= 10:
    if poligono == 3:
        print("é um triangulo.")
    elif poligono == 4:
        print("é um quadrado.")
    elif poligono == 5:
        print("é um pentágono")
    elif poligono == 6:
        print("é um hexágono")
    elif poligono == 7:
        print("é um heptágono")
    elif poligono == 8:
        print("é um octógono")
    elif poligono == 9:
        print("é um eneágono")
    elif poligono == 10:
        print("é um decágono")
else:
    print("erro!!!")

# Exercício 5 - Nome do mês e número de dias

mês = input("digite o mês desejado: ")

if mês == "janeiro" or mês == "Janeiro" or mês == "março" or mês == "Março" or mês == "maio" or mês == "Maio" or mês == "julho" or mês == "Julho" or mês == "agosto" or mês == "Agosto" or mês == "outubro" or mês == "Outubro" or mês == "dezembro" or mês == "Dezembro":
    print("o mês de:", mês,"tem 31 dias")
elif mês == "abril" or mês == "Abril" or mês == "junho" or mês == "Junho" or mês == "setembro" or mês == "Setembro" or mês == "novembro" or mês == "Novembro":
    print("o mês de:", mês,"tem 30 dias")
elif mês == "fevereiro" or mês == "Fevereiro":
    print("o mês de:", mês,"tem 28 ou 29 dias")
else:
    print("invalido!!!")

# Exercício 6 - Classifique o triângulo

lado1 = float(input("digite o número do primeiro lado:"))
lado2 = float(input("digite o número do segundo lado:"))
lado3 = float(input("digite o número do terceiro lado:"))

if lado1 == lado2 == lado3:
    print("o triângulo é equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("o triângulo é isósceles.")
else:
    print("o triângulo é escaleno.")

# Exercício 7 - Níveis de barulho

nivel = float(input("digite o nivel de volume em décibéis: "))
if 40 <= nivel <= 130:
    if nivel == 40:
        print("barulho da sala silenciosa.")
    elif nivel == 70 :
        print("barulho do despertador.") 
    elif nivel == 106 :
        print("barulho do cortador de grama.")
    elif nivel == 130 :
         print("barulho de britadeira.")
    elif nivel >= 40 or nivel <= 70 :
        print("o barulho esta entre o barulho da sala silenciosa e do despertador.")
    elif nivel >= 40 or nivel <= 106 :
        print("o barulho esta entre a sala silenciosa e o cortador de grama.")
    elif nivel >= 40 or nivel <= 130 :
        print("o barulho esta entre a sala silenciosa e a britadeira.") 
    elif nivel >= 70 or nivel <= 106 :
        print("o barulho esta entre o despertador e o cortador de grama.")
    elif nivel >= 70 or nivel <= 130 :
        print("o barulho esta entre o despertador e a britadeira.")
    elif nivel >= 106 or nivel <= 130 :
        print("o barulho esta entre o cortador de grama e a britadeira")
else:
    print("erro!!")

# Exercício 8 - Nota para frequência

#nota para frequencia
nota = input("digite a nota:")
oitava = int(input("digite a oitava da nota:"))

if oitava < 0 or oitava > 8:
    print("não pode ser menor que 0 e maior que 8.")
else:
    if nota == "C":
        frequencia = 261.63
    elif nota == "D":
         frequencia = 293.66
    elif nota == "E":
         frequencia = 329.63
    elif nota == "F":
        frequencia = 349.23
    elif nota == "G":
         frequencia = 392.00
    elif nota == "A":
        frequencia = 440.00
    elif nota == "B":
        frequencia = 493.88
    frequencia_f = frequencia / 2**(4 - oitava)
    print("A frenquência é",frequencia_f)

# Exercício 9 - Data de feriado

feriado = input("digite o dia e o mês desejado:")
if feriado == ["1 de janeiro","21 de abril","1 de maio","7 de setembro","12 de outubro","2 de novembro","15 de novembro","25 de dezembro"]:
    print("correspondem a feriados nacionais.")
elif feriado == "1 de janeiro":
    print("Confraternização universal.")
elif feriado == "21 de abril":
    print("Tiradentes.")
elif feriado == "1 de maio":
    print("Dia do trabalho.")
elif feriado == "7 de setembro":
    print("Independência do Brasil.")
elif feriado == "12 de outubro":
    print("Nossa Senhora Aparecida.")
elif feriado == "2 de novembro":
    print("Finados.")
elif feriado == "15 de novembro":
    print("Proclamação da República")
elif feriado == "25 de dezembro":
    print("Natal")
else:
    print("não corresponde a um feriado nacional.")

# Exercício 10 - Cor da casa do tabuleiro

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

# Exercício 11 - raízes de equação quadrática

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

# Exercicio 12 - Ano bissexto

ano = int(input("digite um ano:"))

if ano % 400 == 0:
    print(ano,"é um ano bissexto.")
elif ano % 100 == 0:
    print(ano,"não é um ano bissexto.")
elif ano % 4 == 0:
    print(ano,"é um ano bissexto.")
else:
    print(ano,"não é um ano bissexto.")
