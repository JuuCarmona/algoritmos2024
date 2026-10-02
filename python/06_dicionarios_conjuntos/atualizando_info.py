estoque ={"caderno universitario":50,"caneta azul":120,"borracha branca":30}

nome_produto = input("Digite o nome o nome do produto:")
nova_quantidade = int(input("Digite o novo valor do produto:"))

if nome_produto in estoque:
    estoque [nome_produto] = nova_quantidade
    print("Quantidade atualizada com sucesso")
    print(estoque)
else:
    print("produto não encontrado no estoque")
