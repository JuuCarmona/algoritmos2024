def countRange(lista,minimo,maximo):
    contador = 0
    for i in range(len(lista)):
        if minimo <= lista[i] and lista[i] < maximo:
            contador = contador + 1
    return contador

def main():
    lista = [1,3,5,7,9,2,4,6,8,10]
    minimo = 3
    maximo = 8
    
    total = countRange(lista,minimo,maximo)
    print(total)

main()
