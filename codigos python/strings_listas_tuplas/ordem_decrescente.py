def ordenar_decrescente(lista):
    lista.sort(reverse=True)

def main():
    numeros = []

    while True:
        numero = int(input("Digite um número inteiro (0 para parar): "))
        if numero == 0:
            break
        numeros.append(numero)

    ordenar_decrescente(numeros)
    print("Números em ordem decrescente:")
    for numero in numeros:
        print(numero)

if __name__ == "__main__":
    main()
