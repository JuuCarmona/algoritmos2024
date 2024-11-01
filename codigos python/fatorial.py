# pede um número
n = int(input("digite o valor de n:"))
# iniciacilizar o acumulador (como é uma multiplicação, o acumulador começa com 1 )
def fatorial_1(n):
    acumulador = 1
# repete de n até 1 com passo -1 (i) 
    for i in range(n,1,-1):
# acumulador = i * acumulador 
        acumulador = i * acumulador
    return acumulador
    
resultado = fatorial_1(n)
print(resultado)
