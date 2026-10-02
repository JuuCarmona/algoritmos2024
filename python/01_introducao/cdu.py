numero = int(input("digite um número inteiro de tres algorismos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print ("centena(s):", centena, "dezena(s):", dezena, "unidade(s):", unidade)
