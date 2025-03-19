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
