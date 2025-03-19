mês = input("digite o mês desejado: ")

if mês == "janeiro" or mês == "Janeiro" or mês == "março" or mês == "Março" or mês == "maio" or mês == "Maio" or mês == "julho" or mês == "Julho" or mês == "agosto" or mês == "Agosto" or mês == "outubro" or mês == "Outubro" or mês == "dezembro" or mês == "Dezembro":
    print("o mês de:", mês,"tem 31 dias")
elif mês == "abril" or mês == "Abril" or mês == "junho" or mês == "Junho" or mês == "setembro" or mês == "Setembro" or mês == "novembro" or mês == "Novembro":
    print("o mês de:", mês,"tem 30 dias")
elif mês == "fevereiro" or mês == "Fevereiro":
    print("o mês de:", mês,"tem 28 ou 29 dias")
else:
    print("invalido!!!")
