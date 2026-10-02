def main():
    numeros = []
    while True:
        entrada = input("Digite um número (pra sair aperte enter): ")
        if entrada == "":
            break
        numeros.append(float(entrada))

    if numeros:
        media = sum(numeros) / len(numeros)
        abaixo_media = [num for num in numeros if num < media]
        acima_media = [num for num in numeros if num > media]
        
        print("\nMédia:", media)
        print("Abaixo da média:", abaixo_media)
        print("Acima da média:", acima_media)
    else:
        print("Nenhum número foi inserido.")

if __name__ == "__main__":
    main()
