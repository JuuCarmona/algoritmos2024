feriado = input("digite o dia e o mês desejado:")
if feriado == ["1 de janeiro","21 de abril","1 de maio","7 de setembro","12 de outubro","2 de novembro","15 de novembro","25 de dezembro"]:
    print("correspondem a feriados nacionais.")
elif feriado == "1 de janeiro":
    print("Confraternização universal.")
elif feriado == "21 de abril":
    print("Tiradentes.")
elif feriado == "1 de maio":
    print("Dia do trabalho.")
elif feriado == "7 de setembro":
    print("Independência do Brasil.")
elif feriado == "12 de outubro":
    print("Nossa Senhora Aparecida.")
elif feriado == "2 de novembro":
    print("Finados.")
elif feriado == "15 de novembro":
    print("Proclamação da República")
elif feriado == "25 de dezembro":
    print("Natal")
else:
    print("não corresponde a um feriado nacional.")
