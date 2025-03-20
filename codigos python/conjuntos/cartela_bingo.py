import random

def gerar_cartela_bingo():
    cartela = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    
    for letra in cartela.keys():
        inicio = 1 if letra == 'B' else 16 if letra == 'I' else 31 if letra == 'N' else 46 if letra == 'G' else 61
        numeros = random.sample(range(inicio, inicio + 15), 5) 
        cartela[letra] = numeros
    
    return cartela

def exibir_cartela_bingo(cartela):
    print(" Cartela de Bingo ")
    print("B   I   N   G   O")
    for i in range(5):
        for letra in cartela.keys():
            print(f"{cartela[letra][i]:2}", end="   ")
        print()

cartela = gerar_cartela_bingo()
exibir_cartela_bingo(cartela)
