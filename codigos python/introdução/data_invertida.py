data = int(input(" digite o dia, o mes e o ano: ")) 

dia = (data // 10000)
print(dia)
resto = data % 10000
mes = (resto  // 100) 
ano = resto  % 100

print("a data:", ano, mes, dia)
