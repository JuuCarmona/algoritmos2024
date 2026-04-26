permissoes_principais = set(input("Digite as permissoes principais:").split())
permissoes_solicitadas = set(input("Digite as permissoes solicitadas:").split())

verificar = permissoes_principais.issubset(permissoes_solicitadas)

if verificar :
    print("As permissões solicitadas fazem parte das permissões principais",verificar)
else:
    print("As permissões solicitadas não fazem parte das permissões principais")
