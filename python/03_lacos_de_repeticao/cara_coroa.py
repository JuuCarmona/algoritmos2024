import random

lancamentos = 0  
simulacoes = 10  

for i in range(simulacoes):
    sequencia_atual = None  
    lancamentos = 0  
    while True:
        resultado = random.choice(['A', 'O'])
        print(resultado, end=' ')

        if sequencia is None:
            sequencia = resultado
        elif sequencia == resultado:
            sequencia = resultado
        else:
            sequencia = resultado
            lancamentos = lancamentos + 1
        
        if lancamentos == 2:
            break
        lancamentos = lancamentos + 1

    print("\nNúmero de lançamentos até 3 resultados iguais consecutivos:", lancamentos + 1)

media = lancamentos / simulacoes
print("Média do número de lançamentos:", media)
