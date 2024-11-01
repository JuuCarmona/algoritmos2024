#criar uma função fatorial(n)
def fatorial(n):
    # se for igual a 1
    if n == 1:
        # retorna 1
        return 1
    # se não 
    else:
        #retorna n * fatorial (n-1)
        return  n* fatorial(n-1)
# pede o numero
n = 20
x = fatorial(n)
# mostra o x
print(x)
