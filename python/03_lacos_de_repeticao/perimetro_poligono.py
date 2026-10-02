import math

perimetro = 0 

x = float(input("digite a coordenada x:"))
y = float(input("digite a coordenada y:"))

x_1 = x
y_1 = y

while True:

    x2 = input("digite a coordenada x (enter para sair):")
    y2 = input("digite a coordenada y(enter para sair):")

    if x2 == ("") or y2 == (""):
        break
    x2 = float(x2)
    y2 = float (y2)

    d = (abs(y2- y_1)**2) + (abs(x2 - x_1)**2)
    d1 = math.sqrt(d)
    
    perimetro = perimetro + d1

    x_1 = x2
    y_1 = y2

    d2 = (abs(y_1 - y)**2) + (abs(x_1 - x))
    d_2 = math.sqrt(d2)

    total = perimetro + d2
    print("O perímetro é:", total)
