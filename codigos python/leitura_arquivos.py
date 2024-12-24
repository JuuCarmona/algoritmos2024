#Peça um arquivo de texto e listar os anos
with open('/home/ifc/Área de trabalho/.Py/exemplo.txt', 'r') as arquivo:
        ano = input("Digite o ano ")
        Incendios = 0
        for linha in arquivo:
            partes = linha.strip().split(',')
            ano = partes[0].strip()
        # Conte os incêndios por ano
            if ano == ano:
              Incendios += int(partes[3])
        # mostre o número de incendios do ano pedido pelo usuário
        print(Incendios)
