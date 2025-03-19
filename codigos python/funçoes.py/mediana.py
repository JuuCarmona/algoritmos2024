def mediana(v1,v2,v3):
    menor = min(v1,v2,v3)
    maior = max(v1,v2,v3)
    média = (v1 + v2 + v3 - menor - maior)
    return média

def main():
    v1 = int(input("digite o valor do primeiro:"))
    v2 = int(input("digite o valor do segundo:"))
    v3 = int(input("digite o valor do terceiro:"))

    média = mediana(v1,v2,v3)
    print("A mediana é:", média)


if __name__ == "__main__":
    main()
