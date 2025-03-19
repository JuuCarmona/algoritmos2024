def obter_prioridade(operador):
    if operador == '+' or operador == '-':
        return 1
    elif operador == '*' or operador == '/':
        return 2
    else:
        return 0

def posfixo(tokens):
    posfixos = []
    operador = []

    for token in tokens:
        if token.isdigit():
            posfixos.append(token)
        elif token == '(':
            operador.append(token)
        elif token == ')':
            while operador[-1] != '(':
                posfixos.append(operador[-1])
                operador = operador[:-1]  
            operador = operador[:-1]  
        else:
            while operador and obter_prioridade(operador[-1]) >= obter_prioridade(token):
                posfixos.append(operador[-1])
                operador = operador[:-1]  
            operador.append(token)

    while operador:
        posfixos.append(operador[-1])
        operador= operador[:-1] 

    return posfixos

def main():
    expressao_infixa = input("Digite a expressão infixa: ")
    tokens = expressao_infixa.split()

    expressao_posfixa = posfixo(tokens)
    print("Expressão pós-fixada:", ' '.join(expressao_posfixa))

if __name__ == "__main__":
    main()
