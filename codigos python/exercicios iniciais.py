# Exercício 1 - Endereço Completo

print("Julia Carmona Guedes Guimarães")
print("Jardim das industrias,São José dos Campos")
print("Rua das Flores,78")

# Exercício 2 - Saudação

n1=input("qual seu nome?")
print("olá", n1)

# Exercício 3 - Área de uma sala

largura=int(input("qual a largura da sala em metros quadrados? "))
profundidade=int(input("qual a profundidade da sala em metros quadrados?"))
area=largura*profundidade
print("area:",area,"metros quadrados")

# Exercício 4 - Área de um terreno

largura=int(input("qual a largura em metros?"))
profundidade=int(input("qual a profundidade em metros?"))

area=largura*profundidade
hectar=area/10000
print("area:",hectar,"hectares")

# Exercício 5 - Retorno de recicláveis

n1=int(input("qual a quantidade de vasilhames de um litro ou menos?"))
n2=int(input("qual a quantidade de vasilhames de um litro ou mais?"))
total=(n1*0.10)+(n2*0.25)
print("o valor total de créditos é R${:.2f}".format(total))

# Exercício 6 - Conta do almoço

rs=int(input("qual o valor da refeição com suco?"))
pp=int(input("qual o valor do prato principal?"))
s=int(input("qual o valor da sobremesa?"))
total=(rs)+(pp)+(s)
print("o valor total da compra é R${:2f}".format(total))

# Exercício 7 - Soma dos primeiros números positivos

n=int(input("digite um numero inteiro positivo:"))
soma=n*(n+1)/2
print(soma)

# Execício 8 - Bugigangas e quinquilharias

bugigangas=int(input("qual a quantidade de bugigangas?"))
quintilharias=int(input("qual a quantidade de quintilharias?"))  
total=(bugigangas*75)+(quintilharias*112) 
print(total)               

# Exercício 9 - Juros compostos

n1=float(input("digite o valor inicial depositado na conta?"))
taxa=12
anos=3
saldo=n1*(taxa)*(anos)
print("saldo",anos,"anos","{:2f}",format(saldo))

# Exercício 10 - Aritmética

import math

a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))

soma = a + b
print("a soma é", soma)

diferenca = a - b 
print("a difereca é", diferenca)

produto = a * b
print("o produto é:", produto)

quociente = a // b
print("o quociente é:", quociente)

resto = a % b
print("o resto é:", resto)

log10a = math.log10(a)
print("o log10a é:", log10a)

ab = a ** b
print(" o resultado de ab é:", ab)

# Exercício 11 - Distância entre dois pontos da terra

import math 

t1=float(input(" digite a latitude do primeiro ponto em graus: "))
g1=float(input("digite a longitude do primeiro ponto em graus: "))
t2=float(input("digite a latitude do segundo ponto em graus: "))
g2=float(input("digite a longitude do segundo ponto em graus: "))

t1r=math.radians(t1)
g1r=math.radians(g1)
t2r=math.radians(t2)
g2r=math.radians(g2)

distancia=6371.01*math.acos(math.sin(t1r)*math.sin(t2r)+math.cos(t1r)*math.cos(t2r)*math.cos(g1r-g2r))

print("a distancia entre os dois pontos é",distancia,"quilômetros.")

# Exercício 12 - Área e volume

import math

r=float(input("digite o valor do raio: "))
              
area=math.pi*r**2

volume=4/3*math.pi*r**3

print("a area é:",area,"o volume é:",volume)

# Exercício 13 - Área de um triângulo

import math

b=float(input("digite o valor da base: "))
h=float(input("digite o valor da altura: "))

area=b*h/2
print("o valor da area é:",area)

# Exercício 14 - import math

l1=float(input("digite o primeiro número: "))
l2=float(input("digite o segundo número: "))
l3=float(input("digite o terceiro número: "))

l=l1+l2+l3/2
area=(l*(l-l1)*(l-l2)*(l-l3))
raiz=math.sqrt(area)

print("a área é:",raiz)

# Exercício 15 - Área de um polígono regular

import math

l=float(input("digite o número do comprimento de um lado:  "))
n=float(input("digite o número de lados: "))

area=n*l**2/4*math.tan(math.pi/n)
print("a area do poligono é:",area)
