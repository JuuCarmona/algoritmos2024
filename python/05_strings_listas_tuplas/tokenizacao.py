def tokenização(expressao):
    tokens = []
    token = ''
    for elemento in expressao:
        if elemento in '+-*/^()':
            if token:
                tokens.append(token)
                token = ''
            tokens.append(elemento)
        elif elemento.isdigit():
            token += elemento
        elif elemento == ' ':
            if token:
                tokens.append(token)
                token = ''
    if token:
        tokens.append(token)
    return tokens

def main():
    expressao = input("Digite uma expressão matemática: ")
    tokens = tokenização(expressao)
    print(tokens)

if __name__ == "__main__":
    main()
