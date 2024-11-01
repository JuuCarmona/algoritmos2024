
# pede dois números
x = int(input("digite o número:"))
y = int(input("digite o número:"))
# vericar o menor e maior número
if x > y:
    print("A ordem é decrescente", x ,",", y)
# se não, inverte a ordem 
else:
    print("A ordem é crescente", y,",",x)


# pede três números
x = int(input("digite um número:"))
y = int(input("digite o número:"))
z = int(input("digite o número:"))
 
# se x < y
if x < y:
    if y < z:
        print(x, y, z)
    elif  x < z:
        print(x ,z ,y)
    else:
        print(z ,x ,y)
else:
    if x < z:
        print(x , y , z)
    elif y < z:
        print(y , z ,x )
    else:
        print(z , y ,x)
