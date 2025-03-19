qt = int(input("digite a quantidade de tempo em segundos: "))

dias = qt // 86400
horas = (qt % 86400)//3600
minutos = ((qt % 86400) % 3600) // 60
segundos = ((qt % 86400) % 3600) % 60

print("dias",dias)
print("horas",horas)
print("minutos",minutos)
print("segundos", segundos)
print("dias:",dias,"horas:",horas,"minutos:",minutos,"segundos:",segundos)
