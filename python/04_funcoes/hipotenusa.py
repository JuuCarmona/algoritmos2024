import math

def hipotenusa(c1,c2):
    soma = c1**2 + c2**2
    total = math.sqrt(soma)
    return total

def main():
    c1 = float(input("digite o cateto 1:"))
    c2 = float(input("digite o cateto 2:"))

    total = hipotenusa(c1,c2)
    print("A hipotenusa é:", total)
main()
