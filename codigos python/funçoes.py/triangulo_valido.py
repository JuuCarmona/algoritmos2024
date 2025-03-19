def triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

def main():
    a = float(input("Digite o comprimento do primeiro canudo: "))
    b = float(input("Digite o comprimento do segundo canudo: "))
    c = float(input("Digite o comprimento do terceiro canudo: "))
    
    if triangulo(a, b, c):
        print("É possível formar um triângulo.")
    else:
        print("Não é possível formar um triângulo.")

if __name__ == "__main__":
    main()
