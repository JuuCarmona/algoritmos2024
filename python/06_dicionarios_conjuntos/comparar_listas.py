lista_laura = set(input("Digite os itens da lista de Laura:").split())
lista_ana = set(input("digite os itens da lista de Ana:").split())

comuns = lista_laura.intersection(lista_ana)
print("itens em ambas as listas:",comuns)

exclusivos_laura = lista_laura.difference(lista_ana)
print("Itens exclusivos de Laura:",exclusivos_laura)

exclusivos_ana = lista_ana.difference(lista_laura)
print("Itens exclusivos de Ana",exclusivos_ana)
