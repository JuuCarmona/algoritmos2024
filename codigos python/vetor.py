import random

#inicia o vetor
vetor = []
#repete quando não houver 10 elementos no vetor
# len = tamanho do vetor
continua = len(vetor) < 10
while continua:
    
    #escolhe um número aleatório
    x = random.randint(1,1000)
    print("número aleatório",x) 
    
    #se x não estiver no vetor
    if x not in vetor:

        #adiciona x no vetor
        vetor.append(x)
        
    continua = len(vetor) < 10
