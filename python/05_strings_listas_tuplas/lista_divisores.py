def lista_divisores(numero):
    if numero <= 0:
        print("O número deve ser positivo.")
        return []

    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    
    divisores = lista_divisores(numero)
    
    if divisores:
        print("Divisores de", numero, "são:", divisores)

if __name__ == "__main__":
    main()
