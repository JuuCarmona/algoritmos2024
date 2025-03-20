import random

def gerar_chamadas_bingo():
    letras = ['B', 'I', 'N', 'G', 'O']
    numeros = [str(i) for i in range(1, 76)]
    chamadas = [letra + numero for letra in letras for numero in numeros]
    return chamadas

def embaralhar_chamadas(chamadas):
    random.shuffle(chamadas)

def linha_zerada(cartela):
    for linha in cartela:
        if all(numero == 0 for numero in linha):
            return True
    return False

def coluna_zerada(cartela):
    for j in range(5):
        if all(cartela[i][j] == 0 for i in range(5)):
            return True
    return False

def diagonal_zerada(cartela):
    if all(cartela[i][i] == 0 for i in range(5)) or all(cartela[i][4-i] == 0 for i in range(5)):
        return True
    return False

def cartela_zerada(cartela):
    return linha_zerada(cartela) or coluna_zerada(cartela) or diagonal_zerada(cartela)

def simular_partida():
    chamadas = gerar_chamadas_bingo()
    embaralhar_chamadas(chamadas)
    cartela = [[0] * 5 for _ in range(5)]
    chamadas_feitas = 0

    while not cartela_zerada(cartela):
        chamada = chamadas.pop(0)
        letra, numero = chamada[0], int(chamada[1:])
        coluna_index = 'BINGO'.index(letra)
        for i in range(5):
            if cartela[i][coluna_index] == numero:
                cartela[i][coluna_index] = 0
                break
        chamadas_feitas += 1

    return chamadas_feitas

def simular_partidas(numero_partidas):
    resultados = []
    for _ in range(numero_partidas):
        resultado_partida = simular_partida()
        resultados.append(resultado_partida)
    minimo = min(resultados)
    maximo = max(resultados)
    media = sum(resultados) / len(resultados)
    return minimo, maximo, media

minimo, maximo, media = simular_partidas(1000)
print("Número mínimo de chamadas:", minimo)
print("Número máximo de chamadas:", maximo)
print("Média de chamadas:", media)
