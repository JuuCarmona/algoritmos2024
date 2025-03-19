import random

def mega_sena():
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    return numeros

def main():
    bilhete = mega_sena()
    print("Números Mega-Sena:")
    for numero in bilhete:
        print(numero, end=" ")
    print()

if __name__ == "__main__":
    main()
