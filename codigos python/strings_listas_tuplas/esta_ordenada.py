def lista_ordenada(lista):
    if lista == sorted(lista):
        return True
    elif lista == sorted(lista,reverse=True):
        return True
    else:
        return False
    
def main():
    numeros = input("digite uma lista de números:")
    lista = [int(num)for num in numeros.split() ]

    if lista_ordenada(lista):
        print("A lista está classificada!")
    else:
        print("A lista não está classificada!")

if __name__ == "__main__":
    main()
