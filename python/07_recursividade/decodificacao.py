def run_length(lista):
    if not lista:
        return []
    else:
        elemento, repeticoes = lista[0]
        return [elemento] * repeticoes + run_length(lista[1:])

def main():
    lista_codificada = (14, 3), (2, 2), (3, 1), (4, 2)
    lista_descompactada = run_length(lista_codificada)
    
    print("Lista em run-length:")
    print(lista_codificada)
    
    print("\nLista descompactada:")
    print(lista_descompactada)

main()
