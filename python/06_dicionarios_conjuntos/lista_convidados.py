convidados = set()

while True:
    nome = input("digite o nome do convidado ou 'sair' para encerrar")

    if nome.lower() == "sair":
        break

    convidados.add(nome)
print (f"convidados confirmados:{','.join(convidados)}")
