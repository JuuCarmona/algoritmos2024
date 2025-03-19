while True:
    entrada = input("Digite uma sequência de 8 bits (ou uma linha em branco para sair): ")

    if entrada == "":
        break

    if not (entrada[:8] == entrada and entrada.count('0') + entrada.count('1') == 8):
        print("Erro: A entrada deve ser uma sequência de 8 bits (0s e 1s).")


    valido = True
    for bit in entrada:
        if bit not in '01':
            valido = False
            break

    if not valido:
        print("Erro: A entrada deve ser uma sequência de 8 bits (0s e 1s).")
    

    num_uns = 0
    for bit in entrada:
        if bit == '1':
            num_uns += 1

    if num_uns % 2 == 0:
        print("O bit deve ser 0.")
    else:
        print("O bit deve ser 1.")
