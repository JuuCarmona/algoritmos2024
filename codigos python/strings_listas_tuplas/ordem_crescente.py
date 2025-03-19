def ordenar_crescente(lista):
    lista.sort()

def main():
    numeros = []

    while True:
        numero = int(input("Digite um número inteiro (0 para parar): "))
        if numero == 0:
            break
        numeros.append(numero)

    ordenar_crescente(numeros)
    
    print("Números em ordem crescente:")
    for numero in numeros:
        print(numero)

if __name__ == "__main__":
    main()
