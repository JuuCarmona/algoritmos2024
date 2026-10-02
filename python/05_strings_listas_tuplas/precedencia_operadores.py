def precedencia(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático (+, -, *, /, ^): ")
    resultado = precedencia(operador)
    if resultado != -1:
        print(f"A precedência é {resultado}.")
    else:
        print("Erro!!!  ")

if __name__ == "__main__":
    main()
