escola = int(input("digite o número de matricula,ano e o semestre que foi matriculado: "))

ano = escola // 10000
semestre = (escola // 1000) % 10

print("ano:", ano,"\nsemestre:", semestre)
