import math

l=float(input("digite o número do comprimento de um lado:  "))
n=float(input("digite o número de lados: "))

area=n*l**2/4*math.tan(math.pi/n)
print("a area do poligono é:",area)
