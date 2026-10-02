dias = int(input("Digite o dia: "))
minutos = int(input("Digite os minutos: "))
horas = int(input("Digite as horas: "))
segundos = int(input("Digite os segundos: "))

total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print("A quantidade de segundos é: ", total)
